from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.paginator import Paginator,EmptyPage

def unauthenticated_user(view_func):
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request,*args,**kwargs)
    return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request,*args,**kwargs):
            group =None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request,*args,**kwargs)
            else:
                return HttpResponse("Your not having permission ... please contact admin")
        return wrapper_func
    return decorator

def admin_only(view_func):
    def wrapper_function(request,*args,**kwargs):
        group =None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'employee':
            return  HttpResponse("Your not having permission ... please contact admin")
        if group == 'admin':
            return view_func(request,*args,**kwargs)    
    return wrapper_function

    

def Paginator_dec(request,*args,**kwargs):
    p=Paginator(args,10)
    page_num = request.GET.get('page',1)
    try:
        return p.page(page_num)
    except EmptyPage:
        return p.page(1)


