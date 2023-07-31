from django.conf import settings
from django.shortcuts import render,redirect
from customer.models import Order, OrderItem

from seller.models import Category, Product
from django.core.mail import send_mail

# Create your views here.
def index(request):
    return render(request,'seller/home.html')

def product(request):
    category=Category.objects.filter(seller_id=request.session['seller_id'])

    msg=''
    if request.method=='POST':
       pname=request.POST['name']
       pcategory=request.POST['category']
       ppro_num=request.POST['pro_num']
       pprice=request.POST['price']
       pstock=request.POST['stock']
       pimage=request.FILES['image']  
       sellerid=request.session['seller_id']

       new_product=Product(name = pname, category_id = pcategory, pro_num = ppro_num, price = pprice,
                            stock = pstock, image = pimage, seller_id = sellerid)

       new_product.save()

       msg='category added successfuly'     

    return render(request,'seller/product.html',{'category':category})

def stock(request):
    return render(request,'seller/stock.html')

def category(request):
    
    category=Category.objects.filter(seller_id=request.session['seller_id'])
    return render(request,'seller/category.html',{'category':category})

def addcat(request):
    msg=''
    if request.method=='POST':
        acat_name = request.POST['cat_name']
        adiscription = request.POST['discription']
        sellerid=request.session['seller_id']

        new_category = Category(catg_name = acat_name, discription = adiscription,seller_id=sellerid)

        new_category.save()

        msg='category added successfuly'

    return render(request,'seller/addcat.html',{'status':msg})

def edit(request,id):
    category=Category.objects.get(id=id)

    if request.method=='POST':
        acat_name = request.POST['cat_name']
        adiscription = request.POST['discription']
        sellerid=request.session['seller_id']

        up_category= Category.objects.filter(id=id).update(catg_name=acat_name,discription=adiscription, seller_id=sellerid)
        
        return redirect('seller:category')

    return render(request,'seller/edit.html',{'category':category})
      
def proview(request):

    product=Product.objects.filter(seller_id=request.session['seller_id'])   
    return render(request,'seller/proview.html',{'product':product})

def delete(request,id):

    cat=Category.objects.get(id=id)
    cat.delete()
    msg='deleted'
    category=Category.objects.filter(seller_id=request.session['seller_id'])
    return render(request,'seller/category.html',{'status':msg,'category':category})

def proedit(request,id):
    product=Product.objects.get(id=id)
   
    category=Category.objects.filter(seller_id=request.session['seller_id'])
    current_category_ids=category.values_list('id',flat=True)

    if request.method=='POST':
         pname=request.POST['name']
         pcategory=request.POST['category']
         ppro_num=request.POST['pro_num']
         pprice=request.POST['price']
         pstock=request.POST['stock']
         pimage=request.FILES['image']  
         sellerid=request.session['seller_id']

         UP_product=Product.objects.filter(id=id).update(name = pname, category_id = pcategory, pro_num = ppro_num, price = pprice,
                            stock = pstock, image = pimage, seller_id = sellerid)
    
         return redirect('seller:product')
    context={
        'product':product,
        'category':category,
        'current_category':current_category_ids
        }
        
    return render(request,'seller/proedit.html',context)

def prodelete(request,id):

    pro=Product.objects.get(id=id)
    pro.delete()
    msg='deleted'
    product=Product.objects.filter(seller_id=request.session['seller_id'])
    return render(request,'seller/proview.html',{'status':msg,'product':product})

def orderview(request):
    seller_id=request.session['seller_id']
    order_items =OrderItem.objects.filter(product__seller_id=seller_id).select_related('order','product')
    orders={}
    for order_item in order_items:
        order =order_item.order
        if order not in orders:
            orders[order]=[]
        orders[order].append(order_item)


    if request.method=='POST':
        order_id=request.POST['order_id']
        action=request.POST['action']

        order=Order.objects.get(id=order_id)
        if action=='confirm':
            send_mail(
                "Order Confirmation",
                "your order has been confirmed . Thank you for purchase . orderid :"+order_id,
                settings.EMAIL_HOST_USER,
                ['mrudhulkrishnamp65@gmail.com'],
                fail_silently=False
            )
            order.order_status='confirmed'
            order.save()
        elif action=='reject':
            send_mail(
                "Order Rejection",
                "your order has been rejected . orderid :"+order_id,
                settings.EMAIL_HOST_USER,
                ['mrudhulkrishnamp65@gmail.com'],
                fail_silently=False
            )
            order.order_status='rejected'
            order.save()

    
    context={
        'orders':orders
    }
    return render(request,'seller/orderview.html',context)

    