from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from .models import Booking


@login_required
def go_to_booking_page(request):
    return redirect('booking_form')