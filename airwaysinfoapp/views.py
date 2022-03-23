from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from airwaysinfoapp.models import (
    Flight,
    Company,
    Plane,
)

from airwaysinfoapp.serializers import (
    FlightSerializer,
    CompanySerializer,
    PlaneSerializer,

)


@api_view(http_method_names=["GET", "POST"])
def api_flights(req):
    if req.method == 'GET':
        flights = Flight.objects.all()
        serializer = FlightSerializer(flights, many=True)
        return Response(serializer.data)
    elif req.method == 'POST':
        serializer = FlightSerializer(data=req.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(http_method_names=["GET", "POST"])
def api_companies(req):
    if req.method == 'GET':
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)
    elif req.method == 'POST':
        serializer = FlightSerializer(data=req.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(http_method_names=["GET", "POST"])
def api_planes(req):
    if req.method == 'GET':
        planes = Plane.objects.all()
        serializer = PlaneSerializer(planes, many=True)
        return Response(serializer.data)
    elif req.method == 'POST':
        serializer = FlightSerializer(data=req.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)