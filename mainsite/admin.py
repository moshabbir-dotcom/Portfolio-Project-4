from django.contrib import admin
from .models import User, Message, Booking
# Register your models here.

# @admin.register(UserProfile)
# class UserProfileAdmin(admin.ModelAdmin):
#     list_display = ('user',)
#     ordering = ('user',)
#     search_fields = ('user',)



@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('fname', 'lname', 'email', 'pnumber')
    list_filter = ('recdate',)
    ordering = ('-recdate',)
    search_fields = ('fname', 'lname', 'email', 'pnumber')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('fname', 'lname', 'email', 'treatment', 'date', 'time')
    list_filter = ('accepted', 'treatment', 'date')
    ordering = ('-date',)
    search_fields = ('fname', 'lname', 'email', 'treatment', 'date', 'time')
    actions = ['accept_booking']

    def accept_booking(self, request, queryset):
        queryset.update(accepted=True)