from django.shortcuts import render
from .models import Menu
from .models import Booking
from .serializers import MenuSerializer
from .serializers import BookingSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import viewsets


# Menu views
def index(request):
  return render(request, 'index.html', {})

class MenuItemView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


# Booking views
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()  # This will fetch all objects from the Booking model
    serializer_class = BookingSerializer  # Set the serializer class to BookingSerializer
