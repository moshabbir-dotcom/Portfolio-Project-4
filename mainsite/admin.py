from django.contrib import admin
from .models import SiteUser, Client, Booking
# Register your models here.

admin.site.register(SiteUser)
admin.site.register(Client)
admin.site.register(Booking)
