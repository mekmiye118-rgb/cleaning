# book/models.py
from django.db import models

class Booking(models.Model):
    SERVICE_CHOICES = [
        ('cleaning', 'Cleaning'),
        ('handyman', 'Handyman'),
        ('delivery', 'Delivery'),
    ]
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    service = models.CharField(max_length=100, choices=SERVICE_CHOICES)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"{self.name} - {self.service} on {self.date}"