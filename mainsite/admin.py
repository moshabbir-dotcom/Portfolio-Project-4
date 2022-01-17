from django.contrib import admin
from .models import SiteUser, Client, Booking
# Register your models here.

#admin.site.register(SiteUser)
admin.site.register(Client)
admin.site.register(Booking)

@admin.register(SiteUser)
class SiteUserAdmin(admin.ModelAdmin):
    list_display = ('fname', 'lname', 'email', 'number')
    ordering = ('fname',)
    search_fields = ('fname', 'lname', 'email', 'number')
