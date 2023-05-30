from django.db import models

# Create your models here.
class categorydb(models.Model):
    Name =models.CharField(max_length=50,null=True,blank=True)
    Email =models.CharField(max_length=50,null=True,blank=True)
    Image =models.ImageField(upload_to="profile")


class Productdb(models.Model):
    categoryname =models.CharField(max_length=60,null=True,blank=True)
    productname =models.CharField(max_length=50,null=True,blank=True)
    quantity =models.IntegerField(null=True,blank=True)
    Price =models.IntegerField(null=True,blank=True)
    Des =models.CharField(max_length=50,null=True,blank=True)
    Image =models.ImageField(upload_to="products")

