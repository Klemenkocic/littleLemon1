from django.test import TestCase
from .models import Menu
from .serializers import MenuSerializer
from rest_framework.test import APIClient

class MenuViewTest(TestCase):
    def setUp(self):
        # Set up some initial menu items
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="Cake", price=120, inventory=50)

    def test_getall(self):
        # Uses the API client to perform a GET request
        client = APIClient()
        response = client.get('/reservation/menu/items/')

        # Get all menu items from the database
        items = Menu.objects.all()
        # Serialize the menu items
        serializer = MenuSerializer(items, many=True)

        # Checks if the response data is equal to the serialized data
        self.assertEqual(response.data, serializer.data)

        # Additionally, check the response status code
        self.assertEqual(response.status_code, 200)
