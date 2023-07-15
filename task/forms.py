from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TaskForm(forms.ModelForm):
    class Meta:
        model=Task
        fields='__all__'




class LoginForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password']

class UserForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=['username','email']
   


    

