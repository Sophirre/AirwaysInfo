# airwaysinfo

DATE = Date; FORMAT: year-month-day 
--------------
Companies 

GET
	http://127.0.0.1:8000/airways/api/companies/

POST
	{
		name: String,
		registration_date: DATE,
		success_flights: Integer,
		rating: Integer(from 1 to 5)

	}

--------------
Planes 

GET 
	http://127.0.0.1:8000/airways/api/planes/

POST
	{
		name: String,
		year_of_manufacture: DATE,
		available_places: Integer.
	}

--------------
Flights 

GET
	http://127.0.0.1:8000/airways/api/flights/

POST 
	{
		start_point: Country/City,
        destination: Country/City,
        transfer_points_amount: Integer,
        company: Integer,
        start_time: DATETTIME
        arriving_time: Integer,
        price: Float,
        plane: Integer,
        available_tickets: Integer
	}

--------------