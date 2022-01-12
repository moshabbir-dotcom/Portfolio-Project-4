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

def provisional_booking(request):
    return render(request, 'provisional_booking.html')

def contact(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        number = request.POST['number']
        message = request.POST['message']

        # NEED TO SEND AN EMAIL FOR SUCCESSFUL CONTACT
        successful_contact = 'Name: " + fname + lname " Phone Number: " + number + " Email: " + email + " Message: " + message'
        
        send_mail(
            'Contact Form Recieved', #Subject
            successful_contact, #Content
            ['email'], #Recipient
        )

        return render(request, 'successful_submission.html', {
            'fname': fname,
            'lname': lname,
            'email': email,
            })

    else:
        return render(request, 'contact.html')


def booking(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        date = request.POST['']
        time = request.POST['']
        addinfo = request.POST['addinfo']

        # NEED TO SEND A CONFIRMATION EMAIL TO USER AND ADMIN
        #send_mail()

        return render(request, 'provisional_booking.html', {
            'fname': fname,
            'email': email,
            'date': date,
            'time': time,
            })

    else:
        return render(request, 'booking_form.html')

