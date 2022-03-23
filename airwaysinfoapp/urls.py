from django.urls import path
from airwaysinfoapp.views import (
    api_flights,
    api_companies,
    api_planes,
)

urlpatterns = [
    path('flights/', api_flights),
    path('companies/', api_companies),
    path('planes/', api_planes),
]