from .models import Booking
from django import forms


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['number_of_people', 'date', 'first_name', 'last_name', 'phone', 'email', 'message']
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }