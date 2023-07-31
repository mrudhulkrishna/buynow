from collections import OrderedDict
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import redirect, render
import razorpay
from commen.models import Customer
from customer.models import Cart, CartItem, Order, OrderItem
from seller.models import Category, Product
from django.db.models import Q

# Create your views here.
def index(request):
    category = Category.objects.all()
    product=Product.objects.all()

    # search bar code
    if request.method == 'POST':
        search_query = request.POST['txt_search']
        product = Product.objects.filter(Q(name__icontains = search_query)|Q(category__discription__icontains = search_query)|Q(category__catg_name__icontains = search_query))
    print(product)
    context={
        'products':product,
        'category':category,
        
    }
        
    return render(request,'customer/home.html',context)

def details(request, id):
    single_product=Product.objects.get(id=id)
    context={
        'single_product':single_product,
      
    }
    return render(request,'customer/details.html',context)

def product_by_category(request,id ):
    category=Category.objects.all()
    product=Product.objects.filter(category_id=id)
    context={
        'products':product,
        'category':category,
    }
    return render(request,'customer/home.html',context)

def filter(request,id):
    produ=Product.objects.filter(category_id=id)

    return render(request,'customer/filter.html',{'product':produ})

def cart_view(request):
    user=Customer.objects.get(id=request.session['customer_id'])

    cart=Cart.objects.get(user_id=user.id)
    print(cart.id)
    items=CartItem.objects.filter(cart_id=cart.id)
    total=0
    for item in items:
         total+=item.product.price*item.quantity

    context={
        'cart':cart,
        'items':items,
        'total':total,
    }
    return render(request,'customer/cart.html',context)

def add_cart(request,product_id):
    product=Product.objects.get(id=product_id)
    cart, _=Cart.objects.get_or_create(user_id=request.session['customer_id'])

    product_exists = CartItem.objects.filter(cart_id=cart.id,product_id=product_id).exists()
    if product_exists:
        item=CartItem.objects.get(cart_id=cart.id,product_id=product_id)
        item.quantity+=1
        item.save()
    else:

        CartItem.objects.create(cart=cart,product=product,quantity=1)
    return redirect('customer:cart')

def remove_cart(request):
    item_id=request.POST['item_id']
    cart=Cart.objects.get(user_id=request.session['customer_id'])
    item=CartItem.objects.get(id=item_id)
    item.delete()
    return JsonResponse({'status':'success'})

def update_quantity(request):
    quantity=request.POST['quantity']
    item_id=request.POST['item_id']
    cart=Cart.objects.get(user_id=request.session['customer_id'])
    items=CartItem.objects.filter(cart_id=cart.id)
    item=CartItem.objects.get(id=item_id)
    item.quantity=quantity
    item.save()
    total_item_price=item.calculate_total_price()
    total=0
    for item in items:
         total+=item.calculate_total_price()
    data={
        'total_item_price':total_item_price ,
        'totl_price':total

    }
    
    return JsonResponse({'status':"success",'data':data})

def order_product(request):
    userid=request.session['customer_id']
    cart=Cart.objects.get(user_id=userid)
    items=CartItem.objects.filter(cart_id=cart.id)
    # products_orderdata=Orders.objects.filter(user_id=userid)
    total=0
    for item in items:
         total+=item.calculate_total_price()
    
    order_amount= total
    order_currency='INR'
    order_receipt='order_rcptid_11'
    notes= {'shipping address':'bommanahalli,bangalore'}
    type(order_amount)
    client=razorpay.Client(auth=(settings.RAZOR_KEY_ID ,settings.RAZOR_KEY_SECRET))
    payment=client.order.create({"amount":order_amount*100,"currency":order_currency,"receipt":order_receipt,'notes':notes})
    print(payment)
    order=Order(user_id=userid,order_no=payment['id'],total_amt=total)
    order.save()
    return JsonResponse(payment)

def updatepayment(request):
    if request.method=='POST':
        print("test test")
        orderid=request.POST['order_id']
        paymentid=request.POST['pay_id']
        signature=request.POST['signatur']
        print(orderid,paymentid,signature)

        #verify the  payment signature
        client=razorpay.Client(auth=(settings.RAZOR_KEY_ID ,settings.RAZOR_KEY_SECRET))
        params_dict={
            "razorpay_order_id":orderid,
            "razorpay_payment_id":paymentid,
            "razorpay_signature":signature
        }
        is_signature_valid=client.utility.verify_payment_signature(params_dict)

        if is_signature_valid:
            print("test**************")
            try:
                order=Order.objects.get(order_no=orderid)
                order.payment_status=True
                order.payment_id=paymentid
                order.signature=signature
               

                cart=Cart.objects.get(user_id=request.session['customer_id'])
                cart_items=CartItem.objects.filter(cart_id=cart.id)

                for item in cart_items:
                    order_item=OrderItem(order_id=order.id,
                                         product_id=item.product.id,
                                         quantity=item.quantity,
                                         price=item.product.price  )
                    order_item.save()
                    order.save()
                    cart_items.delete()
                return JsonResponse({'resp':'success'})
            except Order.DoesNotExist:
                return JsonResponse({'resp':'fail','error':'order not found'})
        else:
            return JsonResponse({'resp':'fail','error':'invalid signature'})
        
    return JsonResponse({'resp':'fail'})

def myorder(request):
    orders=Order.objects.filter(user_id=request.session['customer_id'])
    
    
    
    context={
        "orders":orders
    }
    return render(request,'customer/myorder.html',context)


   
    

