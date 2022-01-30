from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
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


# View for contact form page


def contact(request):
    context = {}
    context['form'] = MessageForm()
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.user = request.user
            message.save()
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
                send_mail(subject, message, 'jasleena@jatherapies.com',
                          ['email'])
            except BadHeaderError:
                return HttpResponse('Invalid Header Found')
            return render(request, 'mainsite/successful_submission.html')
    else:
        return render(request, 'mainsite/contact.html', context)

# View for booking form page


def make_booking(request):
    context = {}
    context['form'] = BookingForm()
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            subject = "JA Therapies Booking Request"
            body = {
                'fname': form.cleaned_data['fname'],
                'lname': form.cleaned_data['lname'],
                'email': form.cleaned_data['email'],
                'treatment': form.cleaned_data['treatment'],
                'date': form.cleaned_data['date'].strftime("%d/%m/%Y"),
                'time': form.cleaned_data['time'],
                'addinfo': form.cleaned_data['addinfo'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'jasleena@jatherapies.com',
                          ['email'])
            except BadHeaderError:
                return HttpResponse('Invalid Header Found')
            return render(request, 'mainsite/successful_submission.html')
    else:
        return render(request, 'mainsite/booking_form.html', context)
