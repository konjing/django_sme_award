from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def loginView(request):

    if request.method == 'POST':        
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('backend-home')
        else:
            messages.info(request, 'User/Password Incorrect')
            return redirect('login')

    context = {}
    return render(request, 'app_backend/login.html', context)

def logoutView(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def homeView(request):

    context = {}
    return render(request, 'app_backend/home.html', context) 

@login_required(login_url='login')
def profileView(request):

    context = {}
    return render(request, 'app_backend/enterpise_profile.html', context)