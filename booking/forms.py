from .models import Booking
from django import forms
from django.utils import timezone


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'number_of_people',
            'date',
            'first_name',
            'last_name',
            'phone',
            'email',
            'message',
        ]

        widgets = {
            'date': forms.TextInput(attrs={'type': 'datetime-local'}),
        }
    
    def clean_date(self):
        date = self.cleaned_data.get('date')

        if date < timezone.now():
            raise forms.ValidationError('The date must be in the future.')

        return date

    def clean_number_of_people(self):
        number_of_people = self.cleaned_data.get('number_of_people')

        if number_of_people < 1:
            raise forms.ValidationError('Number of people must be at least 1.')

        return number_of_people
