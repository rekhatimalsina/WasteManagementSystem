from django.db import models

# Create your models here.
class Registration(models.Model):
    email=models.EmailField(max_length=50,null=0,default=0)
    full_name=models.CharField(max_length=50,null=0,default=0)
    dob=models.DateField(max_length=20)
    password=models.CharField(max_length=50,null=0,default=0)
    confirm_password=models.CharField(max_length=50,null=0,default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


