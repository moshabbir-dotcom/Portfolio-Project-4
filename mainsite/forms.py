from django import forms
from allauth.account.forms import SignupForm, LoginForm
from .models import Message, Booking, User


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['fname', 'lname', 'email', 'pnumber', 'message', ]


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['fname', 'lname', 'treatment', 'date', 'time', 'addinfo', ]


class SignupForm(SignupForm):
    class Meta:
        model = User
        fields = ['username', 'email', ]


class LoginForm(LoginForm):
    class Meta:
        model = User
        fields = ['username', 'email', ]
