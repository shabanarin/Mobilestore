from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms


class RegForm(UserCreationForm):
    class Meta:
        model=User
        fields=[
            'first_name','last_name','email','username','password1','password2','phone','usertype','address'
        ]        
        
        
class LoginForm(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField(widget=forms.PasswordInput)        
                