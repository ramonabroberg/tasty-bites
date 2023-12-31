from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from cloudinary.models import CloudinaryField


class Table(models.Model):
    number = models.IntegerField(unique=True)
    capacity = models.IntegerField()

    def __str__(self):
        return f'Table {self.number} ({self.capacity}p)'

    class Meta:
        ordering = ['number']


class Booking(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='bookings')
    table = models.ForeignKey(
        Table, on_delete=models.CASCADE, related_name='bookings', null=True)
    date = models.DateTimeField()
    number_of_people = models.IntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=25)
    email = models.EmailField(blank=True)
    message = models.TextField(blank=True)
    created_on = models.DateTimeField(default=timezone.now)

    def delete_booking(self):
        self.delete()

    def __str__(self):
        return (
            f'{self.first_name} {self.last_name} - '
            f'{self.date} ({self.number_of_people} people)'
        )

    class Meta:
        ordering = ['date']
