from django.db import models
from commen.models import Customer


from seller.models import Product

# Create your models here.
class Cart(models.Model):
    user =models.OneToOneField(Customer,on_delete=models.CASCADE)
    # created_at =models.DateTimeField(auto_now_add=True)

    
class CartItem(models.Model):
    cart =models.ForeignKey(Cart,on_delete=models.CASCADE, related_name='cart_item')
    product =models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity =models.PositiveIntegerField()

    def calculate_total_price(self):
        return self.product.price*float(self.quantity)
    
class Order(models.Model):
    user=models.ForeignKey(Customer,on_delete=models.CASCADE)
    order_no=models.CharField(max_length=25,unique=True)
    total_amt=models.DecimalField(max_digits=10,decimal_places=2)
    payment_status=models.BooleanField(default=False)
    creat_at=models.DateTimeField(auto_now_add=True)
    payment_id=models.CharField(max_length=25,unique=True,null=True)
    signature=models.CharField(max_length=250,unique=True,null=True)
    order_status=models.CharField(max_length=20,null=True)

class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
