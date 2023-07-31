from django.db import models

from commen.models import Seller

# Create your models here.

class Category(models.Model):
    catg_name =models.CharField(200)
    discription =models.CharField(400)
    seller = models.ForeignKey(Seller,on_delete=models.CASCADE)
    

class Product(models.Model):
    name = models.CharField(200)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    pro_num = models.BigIntegerField()
    price = models.FloatField()
    stock =models.IntegerField()
    image = models.ImageField(upload_to='seller/')
    seller = models.ForeignKey(Seller,on_delete=models.CASCADE)

