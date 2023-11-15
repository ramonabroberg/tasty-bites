from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_filter = ('date',)
    list_display = ('date', 'number_of_people', 'first_name', 'last_name', 'created_on')
    search_fields = ('first_name', 'last_name', 'phone', 'email')
