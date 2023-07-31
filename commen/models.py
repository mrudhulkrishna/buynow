from django.db import models

# Create your models here.

class Seller(models.Model):
    name = models.CharField(max_length = 200)
    email = models.CharField(max_length = 100)
    phone = models.BigIntegerField()
    password = models.CharField(max_length = 100,default='')
    address = models.CharField(max_length = 300)
    ac_no = models.CharField(max_length = 100)
    ifsc = models.CharField(max_length = 100)
    branch = models.CharField(max_length = 200)

class Customer(models.Model):
    first = models.CharField(max_length = 100)
    last = models.CharField(max_length = 100)
    email = models.CharField(max_length = 200)
    password = models.CharField(max_length = 100)
    address = models.CharField(max_length = 300)
    address2 = models.CharField(max_length = 300)
    city = models.CharField(max_length = 100)
    state = models.CharField(max_length = 100)
    country = models.CharField(max_length = 100)
    

