from django.shortcuts import render, redirect, HttpResponse
#from django.core.mail import send_mail
from .models import SiteUser, Message, Booking
from .forms import MessageForm, BookingForm

# Create your views here.

def home(request):
    return render(request, 'mainsite/home.html')

def contact(request):
    if request.method == "POST":
        form = MessageForm(request.POST or None)
        if form.is_valid():
            form.save()
        return render(request, 'mainsite/successful_submission.html')
        #SEND EMAIL
    else:
        return render(request, 'mainsite/contact.html')

def about(request):
    return render(request, 'mainsite/about.html')

def prices(request):
    return render(request, 'mainsite/prices.html')


def successful_submission(request):
    return render(request, 'mainsite/successful_submission.html')

def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST or None)
        if form.is_valid():
            form.save()
        return render(request, 'mainsite/successful_submission.html',)
    else:
        return render(request, 'mainsite/booking_form.html')


def signup(request):
    return render(request, 'allauth/account/signup.html')

def login(request):
    return render(request, 'allauth/account/login.html')

def logout(request):
    return render(request, 'allauth/account/logout.html')

