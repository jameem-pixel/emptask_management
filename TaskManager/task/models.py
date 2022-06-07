import email
from django.db import models
from django.contrib.auth.models import User
from django.forms import Textarea
from datetime import datetime , date
# Create your models here.
class Employee(models.Model):
    user =models.OneToOneField(User,null=True, blank=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=50,null=True,blank=True)
    email = models.EmailField(max_length=20)
    def __str__(self):
        return self.name or ""  
class Taskprovider(models.Model):
    employee=models.ForeignKey(Employee,on_delete=models.CASCADE)
    title=models.CharField(max_length=1000,null=True,blank=True)
    subject=models.CharField(max_length=200,null=True,blank=True)
    date=models.DateField(auto_now_add=False,auto_now=False,null=True,blank=True)



    def __str__(self):
        return self.title or ""






