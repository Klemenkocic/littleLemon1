from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('menu/items', views.MenuItemView.as_view(), name='menu-items-list'),  # Adjusted path to match your URL
    path('menu/<int:pk>', views.SingleMenuItemView.as_view(), name='menu-detail'),
    #path('menu/', views.MenuItemView.as_view(), name='menu-list'),  # Add this line for 'reservation/menu/'

]
