from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
    path('contact.html/', views.contact, name='contact'),
    path('about.html/', views.about, name='about'),
    path('prices.html/', views.prices, name='prices'),
    path('booking_form.html/', views.booking, name='booking_form'),
    path('successful_submission.html/', views.successful_submission, name='successful_submission'),
]