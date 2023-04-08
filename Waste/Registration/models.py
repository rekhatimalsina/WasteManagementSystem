from django.db import models
from django.contrib.auth.models import User

from DriverRegistration.models import RegisterVehicle

# Create your models here.
class Registration(models.Model):
    email=models.EmailField(max_length=50,null=0,default=0)
    full_name=models.CharField(max_length=50,null=0,default=0)
    dob=models.DateField(max_length=20)
    password=models.CharField(max_length=50,null=0,default=0)
    confirm_password=models.CharField(max_length=50,null=0,default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name=models.CharField(max_length=50,null=0,default=0)
    address=models.CharField(max_length=50,null=0,default=0)
    mobile=models.CharField(max_length=15,null=0,default=0)
    photo=models.ImageField(upload_to="static/images/",null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


class AddBin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name= models.CharField(max_length=50,default=0)
    garbage_type=models.CharField(max_length=50,null=0,default=0)
    garbage_image=models.ImageField(upload_to="static/images/",null=True,blank=True)
    area=models.CharField(max_length=50,null=0,default=0)
    latitude =models.CharField(max_length=50,null=0,default=0)
    longitude= models.CharField(max_length=50,null=0,default=0)
    driver = models.ForeignKey(RegisterVehicle, on_delete=models.CASCADE)
    amount=models.CharField(max_length=100,default=0,null=0)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)




    



