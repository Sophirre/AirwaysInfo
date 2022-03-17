from random import randint

FIRST_NAME_INDEX = 0

FLIGHT_TEMPLATES = [
    {
        'start_point': 'Ukraine/Kiev',
        'destination': 'France/Paris',
        'price': randint(2000, 5000),

    },
    {
        'start_point': 'Italy/Rome',
        'destination': 'USA/Texas',
        'price': randint(2000, 3000),
    },
    {
        'start_point': 'USA/Washington',
        'destination': 'Japan/Tokyo',
        'transfer_points_amount': 2,
        'price': randint(3000, 10000),
    },
    {
        'start_point': 'Ukraine/Kiev',
        'destination': 'Ukraine/Lviv',
        'price': randint(1500, 4000),
    },
    {
        'start_point': 'Ukraine/Dnipro',
        'destination': 'Ukraine/Kiev',
        'price': randint(1000, 3000),
    },
]
