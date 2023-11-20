from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from .models import Booking
from .forms import BookingForm


@login_required
def go_to_booking_page(request):
    return redirect('booking_form')


@login_required
def booking_form(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('user_bookings')
    else:
        form = BookingForm()

    return render(request, 'booking_form.html', {'form': form})


@login_required
def user_bookings(request):
    bookings = Booking.objects.filter(user=request.user).order_by('date')
    return render(request, 'user_bookings.html', {'bookings': bookings})
