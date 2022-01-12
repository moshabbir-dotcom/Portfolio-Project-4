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

def contact(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        # NEED TO SEND AN EMAIL
        send_mail(
            'Message from ' + fname, lname,
            + ' about '
            + subject,
            + ' recieved from'
            + email,
            + ' to say: '
            + message,
            ['jasleena@jatherapies.com'],
            )

        return render(request, 'contact.html', {'fname': fname})

    else:
        return render(request, 'contact.html')

