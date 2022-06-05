from email import message
from django.shortcuts import redirect, render
from .forms import TitleForm, Userform
from django.contrib import messages
from . models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .decorators import allowed_users, unauthenticated_user,admin_only
from django.contrib.auth.models import Group
# Create your views here.
unauthenticated_user
def Register(request):
    form =Userform()
    if request.method == 'POST':
        form = Userform(request.POST)
        if form.is_valid():
            user=form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='employee')
            user.groups.add(group)
            employee = Employee()
            employee.user = user
            employee.name = user.username
            employee.email = user.email
            employee.save()
            messages.success(request,'Account was created for'+" "+username )
            return redirect("login")
        else:
            print("something wrong")
    context={'form':form}
    return render(request,'task/reg.html',context)

@login_required(login_url='login')
@admin_only
def main(request):

    context={}
    return render(request,'task/main.html',context)
unauthenticated_user
def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect("common")
        else:   
            messages.warning(request,"Incorrect username or password" )
        print("SOM")
    context = {}
    return render(request,'task/login.html',context)
@login_required(login_url='login')
@allowed_users(allowed_roles=['employee'])
def board(request):
    context = {}
    return render(request,'task/dashboard.html',context)

@login_required(login_url='login')
def Common(request):
    context = {}
    return render(request,'task/common.html',context)


def Logout(request):
    logout(request)
    return redirect('login')