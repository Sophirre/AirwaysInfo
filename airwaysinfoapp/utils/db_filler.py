from faker import Faker
from random import randint

from ..models import (
    Flight,
    Company,
    Plane
)

from .constants import (
    LAST_NAME_INDEX,
    FLIGHT_TEMPLATES,
    PLANES
)

faker = Faker()


def planes_filler():
    planes = [Plane(
        name=plane['name'],
        available_places=plane['available_places'],
        year_of_manufacture=faker.date()
    ) for plane in PLANES]
    Plane.objects.bulk_create(planes)


def companies_filler(companies_amount=10):
    last_name = faker.name().split()[LAST_NAME_INDEX]
    name_endings = ['& Co', 'Airlines', 'Group', f'& {last_name}']
    names = set()
    for _ in range(companies_amount):
        name = f'{last_name} {name_endings[randint(0, len(name_endings)-1)]}'
        names.add(name)
    companies = [Company(
                        name=name,
                        registration_date=faker.date_this_century(),
                        success_flights=randint(10, 1000),
                        rating=randint(1, 5)) for name in names]
    Company.objects.bulk_create(companies)


def flights_creator():
    companies = Company.objects.all()
    planes = Plane.objects.all()
    for company in companies:
        flights = [Flight(**flight_templ) for flight_templ in FLIGHT_TEMPLATES]
        for flight in flights:
            flight.plane = planes[randint(0, len(planes)-1)]

            flight.company = company
            flight.start_time = faker.date_time_this_decade(after_now=True)
            flight.arriving_time = 0
        Flight.objects.bulk_create(flights)


def main():
    planes_filler()
    companies_filler()
    try:
        flights_creator()
    except Exception as e:
        print(e)
