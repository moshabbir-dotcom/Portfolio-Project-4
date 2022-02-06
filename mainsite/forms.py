from django import forms
from .models import Message, Booking


class DateInput(forms.DateInput):
    input_type = 'date'


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['fname', 'lname', 'email', 'pnumber', 'message', ]


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['fname', 'lname', 'email', 'treatment', 'date',
                  'time', 'addinfo', ]
        widgets = {
            'date': DateInput(),
        }
