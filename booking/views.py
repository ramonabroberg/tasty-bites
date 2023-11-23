from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib import messages
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
            messages.success(request, 'Reservation booked successfully!')
            return redirect('user_bookings')
        else:
            return render(request, 'booking_form.html', {'form': form})
    else:
        form = BookingForm()

    return render(request, 'booking_form.html', {'form': form})


@login_required
def user_bookings(request):
    bookings = Booking.objects.filter(user=request.user).order_by('date')
    return render(request, 'user_bookings.html', {'bookings': bookings})


@login_required
def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, 'Reservation updated successfully!')
            return redirect('user_bookings')

    else:
        form = BookingForm(instance=booking)

    return render(
        request, 'edit_booking.html', {'form': form, 'booking': booking}
    )


@login_required
def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    booking.delete()

    messages.success(request, 'Your reservation is now deleted!')
    return redirect('user_bookings')
