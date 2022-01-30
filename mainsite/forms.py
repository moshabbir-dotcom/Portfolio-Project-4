from django import forms
from .models import Message, Booking


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['fname', 'lname', 'email', 'pnumber', 'message', ]


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['fname', 'lname', 'email', 'treatment', 'date',
                  'time', 'addinfo', ]
