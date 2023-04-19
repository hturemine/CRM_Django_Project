from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .form import SignUpForm



def home(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, "Xin chao")
            return redirect('home')
        else:
            messages.success(request, 'Oops, cant login, try again')
            return redirect('home')
    else:
        return render(request, 'home.html', {})

    return render(request, 'home.html', {})

def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request, 'Poipoi, bye bye, bai bai, tam biet,....')
    return redirect('home')

def register_user(request):
    return render(request, 'register.html', {})