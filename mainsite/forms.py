from django import forms
from .models import Message, Booking, SiteUser


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['fname', 'lname', 'email', 'number']


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['fname', 'lname', 'treatment', 'date', 'time', 'addinfo']


# class LoginForm(forms.ModelForm):
#     class Meta:
#         model = SiteUser
#         fields = ['email', 'passwrd']

        