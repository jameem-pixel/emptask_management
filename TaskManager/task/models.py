import email
from turtle import title
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
    requested_by = models.CharField(max_length=50,null=True,blank=True)
    requested_from = models.CharField(max_length=50,null=True,blank=True)
    process = models.CharField(max_length=50,null=True,blank=True)
    PRIORITIES = (
    (0, 'Low'),
    (1, 'Normal'),
    (2, 'High'),)


    priority = models.IntegerField(default=0, choices=PRIORITIES)

    def __str__(self):
        return self.title or ""


class Status_task(models.Model):

    employee=models.ForeignKey(Employee,on_delete=models.CASCADE)
    title=models.ForeignKey(Taskprovider,on_delete=models.CASCADE)

    PRIORITIES_STATUS = (
        ('ASSIGNED', 'assigned'),
        ('INPROGRESS', 'inprogress'),
        ('HOLD', 'hold'),
        ('COMPLETED', 'completed'),
        )
    status = models.CharField(max_length=50,default='ASSIGNED', choices=PRIORITIES_STATUS)
    completeddate=models.DateField(auto_now_add=False,auto_now=False,null=True,blank=True)
    def __str__(self):
        return self.status or ""



