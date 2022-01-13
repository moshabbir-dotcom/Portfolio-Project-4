from django.shortcuts import render
from django.core.mail import send_mail
from .models import Client
from .forms import ClientForm
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'home.html')

def contact(request):
    if request.method == "POST":
        form = ClientForm(request.POST or None)
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

def booking_form(request):
    return render(request, 'booking_form.html')

def successful_submission(request):
    return render(request, 'successful_submission.html')

def provisional_booking(request):
    return render(request, 'provisional_booking.html')


# def booking(request):
#     if request.method == "POST":
#         fname = request.POST['fname']
#         lname = request.POST['lname']
#         email = request.POST['email']
#         date = request.POST['']
#         time = request.POST['']
#         addinfo = request.POST['addinfo']


#         return render(request, 'provisional_booking.html', {

#     else:
#         return render(request, 'booking_form.html')

