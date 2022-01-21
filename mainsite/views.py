from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .models import Message, Booking, User
from .forms import MessageForm, BookingForm, SignupForm

# Create your views here.

def home(request):
    return render(request, 'mainsite/home.html')

def about(request):
    return render(request, 'mainsite/about.html')

def prices(request):
    return render(request, 'mainsite/prices.html')

def successful_submission(request):
    return render(request, 'mainsite/successful_submission.html')

def contact(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            subject = "JA Therapies Contact Request"
            body = {
                'fname': form.cleaned_data['fname'],
                'lname': form.cleaned_data['lname'],
                'email': form.cleaned_data['email'],
                'pnumber': form.cleaned_data['pnumber'],
                'message': form.cleaned_data['fname'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'jasleena@jatherapies.com', ['email'])
            except BadHeaderError:
                return HttpResponse('Invalid Header Found')            
            return render(request, 'mainsite/successful_submission.html')
    else:
        return render(request, 'mainsite/contact.html')

def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            subject = "JA Therapies Booking Request"
            body = {
                'fname': form.cleaned_data['fname'],
                'lname': form.cleaned_data['lname'],
                'email': form.cleaned_data['email'],
                'treatment': form.cleaned_data['date'],
                'time': form.cleaned_data['time'],
                'addinfo': form.cleaned_data['addinfo'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'jasleena@jatherapies.com', ['email'])
            except BadHeaderError:
                return HttpResponse('Invalid Header Found')            
            return render(request, 'mainsite/successful_submission.html')
    else:
        return render(request, 'mainsite/contact.html')


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST or None)
        if form.is_valid():
            form.save()
    return render(request, 'allauth/account/signup.html')


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST or None)
        if form.is_valid():
            form.submit()
        return redirect('mainsite/home.html')
    return render(request, 'allauth/account/login.html')


def logout(request):
    return render(request, 'mainsite/home.html')


def renderdemo(request):
    return render(request, 'mainsite/renderdemo.html')