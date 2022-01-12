from . import views
from django.urls import path, include


urlpatterns = [
    path('', views.home, name='home'),
    path('contact.html/', views.contact, name='contact'),
    path('about.html/', views.about, name='about'),
    path('prices.html/', views.prices, name='prices'),
    path('booking_form.html/', views.booking_form, name='booking_form'),
]