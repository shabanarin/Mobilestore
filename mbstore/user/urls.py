from django.urls import path
from .views import *

urlpatterns = [
    path('uhome/',UserView.as_view(),name='uhome')
]
