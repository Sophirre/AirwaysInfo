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
    arriving_time = md.IntegerField()
    price = md.FloatField()
    plane = md.ForeignKey(
        'Plane',
        on_delete=md.DO_NOTHING,
        related_name='flights',
    )
    available_tickets = md.IntegerField(null=True)

    def __str__(self):
        return f'{self.start_point} -> {self.destination}'


class Company(md.Model):
    name = md.CharField(max_length=32, unique=True)
    registration_date = md.DateField()
    success_flights = md.IntegerField()
    rating = md.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return self.name


class Plane(md.Model):
    name = md.CharField(max_length=300)
    year_of_manufacture = md.DateField()
    available_places = md.IntegerField()

    def __str__(self):
        return self.name
