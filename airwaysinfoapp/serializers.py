from rest_framework import serializers
from airwaysinfoapp.models import (
    Flight,
    Company,
    Plane
)


class FlightSerializer(serializers.ModelSerializer):
    plane = serializers.CharField(source='plane.name')
    company = serializers.CharField(source='company.name')

    class Meta:
        model = Flight
        fields = (
            'start_point', 'destination',
            'transfer_points_amount', 'company',
            'start_time', 'arriving_time',
            'price', 'plane', 'available_tickets',
        )

    def validate(self, data):
        validated_data = super().validated_data(data)
        flight = validated_data.get("name")
        try:
            Flight.objects.get(title=flight)
        except Flight.DoesNotExist:
            print(f"Flight: {flight} DoesNotExist")
        else:
            raise serializers.ValidationError(
                {"error": f"Flight:{flight} already exists"}
            )
        return validated_data


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = (
            'name', 'registration_date',
            'success_flights', 'rating',
        )

    def validate(self, data):
        validated_data = super().validated_data(data)
        company = validated_data.get("name")
        try:
            Company.objects.get(title=company)
        except Flight.DoesNotExist:
            print(f"Company:{company} DoesNotExist")
        else:
            raise serializers.ValidationError(
                {"error": f"Company:{company} already exists"}
            )
        return validated_data


class PlaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plane
        fields = ('name', 'year_of_manufacture', 'available_places')

    def validate(self, data):
        validated_data = super().validated_data(data)
        plane = validated_data.get("name")
        try:
            Plane.objects.get(title=plane)
        except Plane.DoesNotExist:
            print(f"Plane:{plane} DoesNotExist")
        else:
            raise serializers.ValidationError(
                {"error": f"Plane:{plane} already exists"}
            )
        return validated_data
