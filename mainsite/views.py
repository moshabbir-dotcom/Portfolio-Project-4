from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
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
    context ={}
    context['form']= MessageForm()
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
        return render(request, 'mainsite/contact.html', context)

def booking(request):
    context ={}
    context['form']= BookingForm()
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
        return render(request, 'mainsite/contact.html', context)


def signup(request):
    context ={}
    context['form']= SignupForm()
    if request.method == "POST":
        form = SignupForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('')
    return render(request, 'allauth/account/signup.html', context)


def login(request):
    context ={}
    context['form']= AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(request.POST or None)
        if form.is_valid():
            form.submit()
            return redirect('')
    return render(request, 'allauth/account/login.html', context)


def logout(request):
    return render(request, 'mainsite/home.html')
