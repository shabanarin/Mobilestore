from django.urls import path
from .views import *

urlpatterns = [
    path('stre/',StoreHome.as_view(),name='storehome'),
    path('addpro/',AddProView.as_view(),name='addproduct'),
    path('viewpro/',ProductView.as_view(),name='viewproduct'),
    path('dltpro/<int:did>',DeleteProd.as_view(),name='dltpro'),
    path('editpro/<int:did>',EditProd.as_view(),name='edtprod')
    
    
    
]   