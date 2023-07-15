from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages

def home(request):
    return render(request,'home.html')

def tasks(request):
    if request.method=="POST":
        tasks=Task.objects.all()
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'tasks.html',{'tasks':tasks,'form':form})
    
    form=TaskForm(request.POST)
    tasks=Task.objects.all()
    return render(request,'tasks.html',{'tasks':tasks,'form':form})

def update(request,id):
    id=Task.objects.get(pk=id)
    if request.method=="POST":
        form=TaskForm(request.POST,instance=id)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    form=TaskForm(request.POST,instance=id)
    return render(request,'update.html',{'form':form})

def delete(request,id):
    id=Task.objects.get(pk=id)
    id.delete()
    return redirect('tasks')

def register(request):
    if request.method=="POST":
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,'user created successfully')
            return render(request,'register.html',{'form':form})
    
    form=UserForm()
    return render(request,'register.html',{'form':form})

def loginpage(request):
    if request.method=="POST":
        user=request.POST['username']
        pass1=request.POST['password']
        
        user=authenticate(username=user,password=pass1)
        if user is not None:
            login(request,user)
            messages.info(request,'user login successful')
            return redirect('home')
    
    return render(request,'login.html')

def logoutpage(request):
    logout(request)
    return redirect('home')
