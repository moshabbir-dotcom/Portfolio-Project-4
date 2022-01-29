from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from allauth.account.forms import SignupForm, LoginForm
from .models import Message, Booking
from .forms import MessageForm, BookingForm

# Create your views here.

# Views for all static pages


def home(request):
    return render(request, 'mainsite/home.html')


def about(request):
    return render(request, 'mainsite/about.html')


def prices(request):
    return render(request, 'mainsite/prices.html')


def successful_submission(request):
    return render(request, 'mainsite/successful_submission.html')


def logout(request):
    return render(request, 'mainsite/home.html')


# View for allauth signup page
def signup(request):
    context = {}
    context['form'] = SignupForm()
    if request.method == "POST":
        form = SignupForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('mainsite/home.html')
    return render(request, 'allauth/account/signup.html', context)

# View for allauth login page


def login(self, *args, **kwargs):
    if request.method == "POST":
        form = LoginForm(request.POST or None)
        if form.is_valid():
            form.submit()
            return redirect('mainsite/home.html')
    return render(request, 'allauth/account/login.html')

# View for contact form page


def contact(request):
    context = {}
    context['form'] = MessageForm()
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

# View for booking form page


def booking(request):
    context = {}
    context['form'] = BookingForm()
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
