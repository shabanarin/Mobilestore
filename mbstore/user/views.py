from django.shortcuts import render,redirect
from django.views.generic import View,CreateView,TemplateView,FormView,UpdateView
from store.models import StoreModel
from django.contrib import messages

# Create your views here.
class UserView(View):
    def get(self,request):
        prod=StoreModel.objects.all()
        return render(request,'userhome.html',{'data':prod})