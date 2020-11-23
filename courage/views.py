from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

def home(request):
    if request.method == 'GET':
        return render(request, 'courage/home.html', {})



def register_user(request):
    if request.method == 'POST':
        email       = request.POST['email']
        first_name  = request.POST['first_name']
        last_name   = request.POST['last_name']
        username    = request.POST['username']
        password    = request.POST['password']
        
        user = User.objects.create_user(email=email, first_name=first_name, last_name=last_name, username=username, password=password)
        if user is not None:
            messages.success(request, 'Registration successful.')
            login(request, user)
            return render(request, 'courage/login.html', {})
        else:
            messages.success(request, 'Registration failed, please try again...')
            return render(request, 'courage/register.html', {})
    else:
        return render(request, 'courage/register.html', {})



def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            messages.success(request, 'Login successful.')
            login(request, user)
            return render(request, 'courage/home.html', {})
        else:
            messages.success(request, 'Login failed, please try again...')
            return render(request, 'courage/login.html', {})
    else:
        return render(request, 'courage/login.html', {})




def logout_view(request):
    print('got the flow')
    logout(request)
    messages.success(request, 'Logout successful')
    return render(request, 'courage/login.html', {})
