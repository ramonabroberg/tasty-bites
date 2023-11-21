from . import views
from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path(
        '',
        TemplateView.as_view(template_name='index.html'),
        name='home'
    ),
    path(
        'booking_form/',
        views.booking_form,
        name='booking_form'
    ),
    path(
        'user_bookings/',
        views.user_bookings,
        name='user_bookings'
    ),
    path(
        'go_to_booking_page/',
        views.go_to_booking_page,
        name='go_to_booking_page'
    ),
    path(
        'edit_booking/<int:booking_id>/',
        views.edit_booking,
        name='edit_booking'
    ),
    path(
        'delete_booking/<int:booking_id>/',
        views.delete_booking,
        name='delete_booking'
    ),
]
