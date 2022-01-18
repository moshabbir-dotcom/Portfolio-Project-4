from django.shortcuts import render, redirect, HttpResponse
#from django.core.mail import send_mail
from .models import SiteUser, Message, Booking
from .forms import MessageForm, BookingForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def contact(request):
    if request.method == "POST":
        form = MessageForm(request.POST or None)
        if form.is_valid():
            form.save()
        return render(request, 'successful_submission.html')
        #SEND EMAIL
    else:
        return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def prices(request):
    return render(request, 'prices.html')


def successful_submission(request):
    return render(request, 'successful_submission.html')

def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST or None)
        if form.is_valid():
            form.save()
            return render(request, 'successful_submission.html',)
        else:
            return render(request, 'booking_form.html')

