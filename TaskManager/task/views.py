from email import message
from multiprocessing import context
from turtle import st
from unicodedata import name
from django.shortcuts import redirect, render
from urllib3 import Retry
from .forms import TitleForm, Userform,Statusform
from django.contrib import messages
from . models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .decorators import allowed_users, unauthenticated_user,admin_only,Paginator_dec
from django import template
register = template.Library()
from django.contrib.auth.models import Group
from django.core.paginator import Paginator,EmptyPage
from datetime import datetime,timedelta
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
    task = Taskprovider.objects.all().order_by('-priority')
    form = TitleForm()
    p=Paginator(task,10)
    page_num = request.GET.get('page',1)
    try:
        page=p.page(page_num)
    except EmptyPage:
        page=p.page(1)
    if request.method =='POST':
        form = TitleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    context={'form':form,'page':page}
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
    user_query=Employee.objects.filter(name=request.user)
    cur_id=user_query[0].id
    st_form=Statusform()
    if request.method =='POST':
        st_form=Statusform(request.POST)
        if st_form.is_valid():
            st_form.save()
        else:
            messages.warning(request,"Already submited Please do update")
    tk=Taskprovider.objects.filter(employee_id=cur_id)
    p=Paginator(tk,10)
    page_num = request.GET.get('page',1)
    try:
        page1=p.page(page_num)
    except EmptyPage:
        page1=p.page(1)
    
    tkc=Status_task.objects.filter(status='COMPLETED').filter(employee_id=cur_id)
    p=Paginator(tkc,10)
    page_num = request.GET.get('page',1)
    try:
        page3=p.page(page_num)
    except EmptyPage:
        page3=p.page(1)
    tkinp=Status_task.objects.filter(status='INPROGRESS').filter(employee_id=cur_id)
    p=Paginator(tkinp,10)
    page_num = request.GET.get('page',1)
    try:
        page2=p.page(page_num)
    except EmptyPage:
        page2=p.page(1)
    tkh=Status_task.objects.filter(status='HOLD').filter(employee_id=cur_id)
    p=Paginator(tkh,10)
    page_num = request.GET.get('page',1)
    try:
        page4=p.page(page_num)
    except EmptyPage:
        page4=p.page(1)
    context={"emp":page1,"st_form":st_form,'tkinp':page2,"tkc":page3,'tkh':page4}
    return render(request,'task/dashboard.html',context)

@login_required(login_url='login')
def Common(request):
    st=[]
    user_query=Employee.objects.all()
    for i in user_query:
        k=i.id
        st.append(Status_task.objects.filter(employee_id=k))
    flat_list = [x for xs in st for x in xs]
    
    context={'st':flat_list}
    return render(request,'task/common.html',context)

@login_required(login_url='login')
@admin_only
def Update(request, pk):
    tasks =Taskprovider.objects.get( id = pk)
    form = TitleForm(instance=tasks)
    context = {'tasks':tasks, 'form':form}
    
    if request.method == 'POST':
        form = TitleForm(request.POST, instance=tasks)
        if form.is_valid():
            form.save()
        return redirect("/")
    return render(request,'task/update_task.html',context)



@login_required(login_url='login')
@admin_only
def Delete(request, pk):
    item = Taskprovider.objects.get(id = pk)
    context = {'item':item}
    if request.method == 'POST':
        item.delete()
        return redirect("/")    
    return render (request,'task/del.html', context)

def Logout(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
@allowed_users(allowed_roles=['employee'])
def Update_task(request, pk):
    tasks =Status_task.objects.get( taskprovider = pk)
    form = Statusform(instance=tasks)
    context = {'emp':tasks, 'form':form}
    
    if request.method == 'POST':
        form = Statusform(request.POST, instance=tasks)
        if form.is_valid():
            form.save()
        return redirect("common")    
    return render(request,'task/updatetask.html',context)
