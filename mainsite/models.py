from django.db import models

# Create your models here.
class Client(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    number = models.CharField(max_length=16, null=True)

    def __str__(self):
        return self.fname + ' ' + self.lname + ' ' + self.number + ' ' + self.email


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


class Booking(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    date = models.DateField(auto_now_add=False, null=True, blank=True)
    sent_date = models.DateField(auto_now_add=True)
    accepted = models.BooleanField(default=False)
    accepted_date = models.DateTimeField(auto_now=False, null=True, auto_now_add=False,)
    user = models.ForeignKey(Client, blank=True, null=True, on_delete=models.CASCADE)
    time = models.CharField(max_length=50, choices = TIMESLOT_CHOICES, default='08:00-09:00')
    addinfo = models.TextField(max_length= 1000, blank=True)

    def __str__(self):
        return self.fname + ' ' + self.lname + ' ' + self.email + ' '

    class Meta:
        ordering = ['-sent_date']