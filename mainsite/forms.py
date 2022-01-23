from django import forms
from .models import Message, Booking, User


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['fname', 'lname', 'email', 'pnumber', 'message']


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['fname', 'lname', 'treatment', 'date', 'time', 'addinfo']


class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email', 'password']

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

        