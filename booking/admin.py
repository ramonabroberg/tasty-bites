from django.contrib import admin
from .models import Booking, Table


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_filter = ('number', 'capacity')
    list_display = ('number', 'capacity')
    search_fields = ('number',)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_filter = ('date',)
    list_display = ('id', 'date', 'table', 'number_of_people', 'first_name', 'last_name', 'created_on')
    search_fields = ('id', 'first_name', 'last_name', 'phone', 'email')
