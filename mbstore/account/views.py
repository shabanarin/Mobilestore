from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,FormView
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.urls import reverse_lazy
from .models import User
from .forms import *

# Create your views here.
class Home(TemplateView):
    template_name="home.html"
    
    
class RegView(CreateView):
    template_name="reg.html" 
    model=User
    form_class=RegForm 
    success_url=reverse_lazy('home')
    
def POST(self,request,*args,**kwargs):
    form_data=self.form_class(request.POST)
    if form_data.is_valid():
        messages.success(request,"Registerion Completed!!")
        return redirect('home')
    else:
        messages.success(request,"Registerion Failed!!")
        return redirect('home')    
        
        
        
class LoginView(FormView):
    template_name="login.html"
    form_class=LoginForm
    def post(self,request):
        uname=request.POST.get("username")
        psw=request.POST.get("password")
        user=authenticate(request,username=uname,password=psw)
        if user:
            if user.usertype=="store":
               login(request,user)
               return redirect("storehome")
            login(request,user)
            return redirect("uhome")
        else: 
            messages.error(request,"incorrect password") 
            return redirect("log")        