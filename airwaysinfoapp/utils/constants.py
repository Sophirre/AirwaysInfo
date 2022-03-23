from random import randint

LAST_NAME_INDEX = 1

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

PLANES = [{'name': 'Airbus A310', 'available_places': 183},
          {'name': 'Airbus A320', 'available_places': 259},
          {'name': 'Airbus A330', 'available_places': 440},
          {'name': 'Boeing-737', 'available_places': 114 },
          {'name': 'Boeing-747', 'available_places': 370},
          {'name': 'Boeing-767', 'available_places': 385},
          {'name': 'Boeing-777', 'available_places': 235},

          ]