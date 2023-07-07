from django.db import models
from django.contrib.auth.models import AbstractUser,User

# Create your models here.
class User(AbstractUser):
    phone=models.IntegerField(null=True)
    options=[
        ('store','store'),
        ('n_user','n_user')
    ]
    usertype=models.CharField(max_length=100,choices=options,default='n_user')
    address=models.TextField()
    