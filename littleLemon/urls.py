"""
URL configuration for littleLemon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from reservation import views  # Import the views from your reservation app

# Create a router and register the viewsets with it.
router = DefaultRouter()
router.register('booking/tables', views.BookingViewSet, basename='booking')  # Updated line

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reservation/', include('reservation.urls')),
    path('reservation/booking/', include(router.urls)),  
    path('reservation/', include(router.urls)),  # Include the router URLs under the 'reservation/' path
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken'))
]
