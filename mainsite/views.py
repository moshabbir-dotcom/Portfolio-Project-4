from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .models import Booking
from .forms import MessageForm, BookingForm
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template
import os

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


@login_required
def manage_booking(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'mainsite/manage_booking.html',
                  {"bookings": bookings})

# View for contact form page


@login_required
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
                'message': form.cleaned_data['message'],
            }
            message = get_template("mainsite/contact_email.html").render(body)

            try:
                send_mail(subject, message, form.cleaned_data['email'],
                          [os.environ["EMAIL_HOST_USER"]])
            except BadHeaderError:
                return HttpResponse('Invalid Header Found')
            return render(request, 'mainsite/successful_submission.html')
    else:
        return render(request, 'mainsite/contact.html', context)

# View for booking form page


@login_required
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
            message = get_template("mainsite/booking_email.html").render(body)

            try:
                send_mail(subject, message, os.environ["EMAIL_HOST_USER"],
                          [os.environ["EMAIL_HOST_USER"], form.cleaned_data['email']])
            except BadHeaderError:
                return HttpResponse('Invalid Header Found')
            return render(request, 'mainsite/successful_submission.html')
    else:
        return render(request, 'mainsite/booking_form.html', context)


@login_required
def delete_booking(request, id):
    booking = Booking.objects.get(id=id)
    if booking.user != request.user:
        return redirect('manage_booking')
    booking.delete()
    return redirect('manage_booking')


@login_required
def edit_booking(request, id):
    context = {}
    booking = Booking.objects.get(id=id)
    if booking.user != request.user:
        return redirect('manage_booking')
    context['form'] = BookingForm(instance=booking)

    if request.method == "POST":
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            subject = "JA Therapies Updated Booking Request"
            body = {
                'fname': form.cleaned_data['fname'],
                'lname': form.cleaned_data['lname'],
                'email': form.cleaned_data['email'],
                'treatment': form.cleaned_data['treatment'],
                'date': form.cleaned_data['date'].strftime("%d/%m/%Y"),
                'time': form.cleaned_data['time'],
                'addinfo': form.cleaned_data['addinfo'],
            }
            message = get_template("mainsite/booking_email.html").render(body)

            try:
                send_mail(subject, message, os.environ["EMAIL_HOST_USER"],
                          ['email'])
            except BadHeaderError:
                return HttpResponse('Invalid Header Found')
            return render(request, 'mainsite/successful_submission.html')
    else:
        return render(request, 'mainsite/booking_form.html', context)
