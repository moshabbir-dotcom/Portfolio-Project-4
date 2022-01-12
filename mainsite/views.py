from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.

def home(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def prices(request):
    return render(request, 'prices.html')

def booking_form(request):
    return render(request, 'booking_form.html')

def successful_submission(request):
    return render(request, 'successful_submission.html')

def contact(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        # NEED TO SEND AN EMAIL
        #send_mail()

        return render(request, 'successful_submission.html', {'fname': fname})

    else:
        return render(request, 'contact.html')


def booking(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        date = request.POST['date']
        time = request.POST['time']
        addinfo = request.POST['addinfo']

        # NEED TO SEND A CONFIRMATION EMAIL TO USER AND ADMIN
        #send_mail()

        return render(request, 'successful_submission.html', {'fname': fname})

    else:
        return render(request, 'booking_form.html')

