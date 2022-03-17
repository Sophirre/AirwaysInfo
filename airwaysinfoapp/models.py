from django.db import models as md
from django.core.validators import MinValueValidator, MaxValueValidator


class Flight(md.Model):
    start_point = md.CharField(max_length=100)
    destination = md.CharField(max_length=100)
    transfer_points_amount = md.IntegerField(default=0, blank=True)
    company = md.ForeignKey(
        'Company',
        on_delete=md.CASCADE,
        related_name='flights'
    )
    start_time = md.DateTimeField()
    arriving_time = md.TimeField()
    price = md.FloatField()

    def __str__(self):
        return f'{self.start_point} -> {self.destination}'


class Company(md.Model):
    name = md.CharField(max_length=32, unique=True)
    registration_date = md.DateField()
    success_flights = md.IntegerField()
    rating = md.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
