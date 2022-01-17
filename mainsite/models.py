from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class SiteUser(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    number = models.CharField(max_length=11, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    passwrd = models.CharField(max_length=50)

    def __str__(self):
        return self.fname + ' ' + self.lname + ' ' + self.number + ' ' + self.email

    class Meta:
        ordering = ['-fname', 'lname']


class Client(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    number = models.CharField(max_length=11, null=True, unique=True)
    message = models.CharField(max_length=1000, blank=True, null=True)
    recdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fname + ' ' + self.lname + ' ' + self.number + ' ' + self.email + ' '

    class Meta:
        ordering = ['-recdate']


TIMESLOT_CHOICES = (
    ('08:00-09:00', '08:00 to 09:00'),
    ('09:00-10:00', '09:00 to 10:00'),
    ('10:00-11:00', '10:00 to 11:00'),
    ('11:00-12:00', '11:00 to 12:00'),
    ('12:00-13:00', '12:00 to 13:00'),
    ('13:00-14:00', '13:00 to 14:00'),
    ('14:00-15:00', '14:00 to 15:00'),
    ('15:00-16:00', '15:00 to 16:00'),
    ('16:00-17:00', '16:00 to 17:00'),
)

THERAPY_CHOICES = (
    ('physical_therapy', 'Physical Therapy -£45'),
    ('sports_massage_therapy', 'Sports Massage Therapy -£45'),
    ('fire_cupping_therapy', 'Fire Cupping Therapy -£50'),
    ('swedish_massage_therapy', 'Swedish Massage Therapy -£45'),
    ('aroma_therapy', 'Aromatherapy -£45'),
    ('wet_cupping_therapy', 'Wet Cupping Therapy -£45'),
    ('graston_therapy', 'Graston IATM Therapy -£45'),
    ('nutrition_therapy', 'Nutritional Therapy -£45'),
)


class Booking(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    treatment = models.CharField(max_length=100, choices = THERAPY_CHOICES, default='Physical Therapy -£45')
    date = models.DateField(auto_now_add=False, null=True)
    sent_date = models.DateField(auto_now_add=True)
    time = models.CharField(max_length=50, choices = TIMESLOT_CHOICES, default='08:00-09:00')
    accepted = models.BooleanField(default=False)
    user = models.ForeignKey(SiteUser, null=True, on_delete=models.CASCADE)
    addinfo = models.TextField(max_length= 1000, blank=True, null=True)

    def __str__(self):
        return self.fname + ' ' + self.lname + ' ' + self.email + ' '

    class Meta:
        ordering = ['-sent_date']