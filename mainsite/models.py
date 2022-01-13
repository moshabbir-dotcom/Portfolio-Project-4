from django.db import models

# Create your models here.
class Client(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    number = models.CharField(max_length=16, null=True)

    def __str__(self):
        return self.fname + ' ' + self.lname + ' ' + self.number + ' ' + self.email