from django import forms
from .models import Client, Booking


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['fname', 'lname', 'email', 'number']


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['fname', 'lname', 'date', 'time', 'addinfo']