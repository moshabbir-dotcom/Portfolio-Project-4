from django.shortcuts import render, redirect
# from django.contrib.auth import allauth
from django.contrib import messages

# Create your views here.


def login_user(request):
    if request.method == "POST":
        email = request.POST['email']
        passwrd = request.POST['passwrd']
        user = authenticate(request, email=email, passwrd=passwrd)
        if user is not None:
            login(request, user)
            return redirect('home.html')
        else:
            messages.success(request, "Login error... Please try again")
            return redirect('login.html')

    return render(request, 'authenticate/login.html')


def logout_user(request):
    logout(request)
    messages.success(request, "Login error... Please try again")
    return redirect('login.html')