from atexit import register
from django.contrib import admin
from . models import *
# Register your models here.
admin.site.register(Employee)
admin.site.register(Taskprovider)
admin.site.register(Status_task)

