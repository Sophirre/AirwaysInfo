from faker import Faker
from random import randint

from ..models import (
    Flight,
    Company,
)

from .constants import (
    FIRST_NAME_INDEX,
    FLIGHT_TEMPLATES,
)

faker = Faker()


def companies_filler(companies_amount=10):
    names = set()
    for _ in range(companies_amount):
        name = faker.name().split()[FIRST_NAME_INDEX]
        names.add(name)
    companies = [Company(
                        name=name,
                        registration_date=faker.date_this_century(),
                        success_flights=randint(10, 1000),
                        rating=randint(1, 5)) for name in names]
    print('run')
    Company.objects.bulc_create(companies)


def flights_creator():
    companies = Company.object.all()
    for company in companies:
        flights = [Flight(**flight_templ) for flight_templ in FLIGHT_TEMPLATES]
        for flight in flights:
            flight.company = company
            flight.start_time = faker.date_time_this_decade(after_now=True)
            flight.arriving_time = 0
        Flight.objects.bulc_create(flights)
