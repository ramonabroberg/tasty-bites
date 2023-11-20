from . import views
from django.urls import path
from django.views.generic import TemplateView
from .views import go_to_booking_page, booking_form, user_bookings

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('booking_form/', booking_form, name='booking_form'),
    path('user_bookings/', user_bookings, name='user_bookings'),
    path('go_to_booking_page/', go_to_booking_page, name='go_to_booking_page'),
]