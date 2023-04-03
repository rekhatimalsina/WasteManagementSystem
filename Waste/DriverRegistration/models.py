from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class RegisterVehicle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle_no=models.CharField(unique=True ,max_length=50,default=0)
    vehicle_type=models.CharField(max_length=50,default=0)
    driver_name=models.CharField(max_length=50,default=0)
    driver_photo=models.ImageField(upload_to="static/images/",null=True,blank=True)
    driver_license_no=models.CharField(unique=True ,max_length=50,default=0)
    license_photo=models.ImageField(upload_to="static/images/",null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)