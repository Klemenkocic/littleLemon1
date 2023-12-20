from rest_framework import serializers
from .models import Menu 
from django.contrib.auth.models import User
from .models import Booking  # Import the Booking model from your models.py file


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'  # This will include all model fields in the serializer


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking  # Specify that we're using the Booking model
        fields = '__all__'  # Include all fields from the Booking model
