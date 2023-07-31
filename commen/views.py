from django.shortcuts import render,redirect

from .models import Customer, Seller

# Create your views here.
def index(request):
    return render(request,'commen/home.html')

def admin(request):
    return render(request,'commen/admin.html')

def seller(request):
    msg = ''
    if request.method == 'POST':
        sname = request.POST['name']
        semail = request.POST['email']
        sphone = request.POST['phone']
        spassword = request.POST['password']
        saddress = request.POST['address']
        sacc_no = request.POST['acc_no']
        sifsc = request.POST['ifsc']
        sbranch = request.POST['branch']

        new_seller = Seller(name = sname, email = semail, phone = sphone,
                            password = spassword, address = saddress, ac_no = sacc_no,
                            ifsc = sifsc, branch = sbranch)
        new_seller.save()
        msg = " seller added succesfully"

    return render(request,'commen/seller.html',{'status':msg})

def cust(request):
    msg = ''
    if request.method == 'POST':
        cfirst = request.POST['first']
        clast = request.POST['last']
        cemail = request.POST['email']
        cpassword =request.POST['password']
        caddress = request.POST['address']
        caddress2 = request.POST['address2']
        ccity = request.POST['city']
        cstate = request.POST['state']
        ccountry = request.POST['country']

        new_customer = Customer(first = cfirst, last = clast, email= cemail, password = cpassword,
                                address = caddress, address2 = caddress2, city = ccity, state = cstate,
                                country = ccountry)
        new_customer.save()
        msg = "Customer Added Succesfully"

    return render(request,'commen/customer.html',{'status':msg})

def sello(request):
    msg=''
    if request.method=='POST':
        suser=request.POST['user']
        spassword=request.POST['password']

        try:
            seller=Seller.objects.get(email=suser,password=spassword)
            request.session['seller_id']=seller.id
            return redirect('seller:home')
        except:
            msg='invalide username or password'
    return render(request,'commen/sell_log.html',{'status':msg})  

def custo(request):
    msg=''
    if request.method=='POST':
        cuser=request.POST['user']
        cpassword=request.POST['password']

        # try:
        customer=Customer.objects.get(email=cuser,password=cpassword)
        request.session['customer_id']=customer.id
        return redirect('customer:home')
        # except:
        #     msg='invalide username or password'
    return render(request,'commen/cust_log.html',{'status':msg})  

