from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status

from restaurant.models import Menu
from restaurant.serializers import MenuItemSerializer
from restaurant.views import *
from rest_framework.test import APIClient
from django.utils import timezone

class MenuItemViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username = 'testuser', password = 'testpassword')
        self.pizza = Menu.objects.create(title = 'Pizza', price = 12.99, inventory = 10)
        self.burger = Menu.objects.create(title = 'burger', price = 8.99, inventory = 5)
        self.pasta = Menu.objects.create(title = 'Pasta', price = 15.99, inventory = 7)
        self.url_list = reverse('menu-list')
        self.url_detail = lambda pk: reverse('menu-detail', args=[pk])
        
    def test_get_all_menu_items(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        menu_items = Menu.objects.all()
        serializer = MenuItemSerializer(menu_items, many=True)
        self.assertEqual(response.json(), serializer.data)
        
    def test_get_single_menu_item(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.url_detail(self.pizza.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        serializer = MenuItemSerializer(self.pizza)
        self.assertEqual(response.json(), serializer.data)
        
class BookingViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.booking1 = Booking.objects.create(name='John Doe', booking_date = timezone.now(), no_of_guests=2)
        self.booking2 = Booking.objects.create(name='Jane Doe', booking_date = timezone.now(), no_of_guests=4)
        self.url_list = reverse('booking-list')
        self.url_detail = lambda pk: reverse('booking-detail', args=[pk])
        
    def test_get_all_bookings(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        self.assertEqual(response.json(), serializer.data)
        
    def test_create_booking(self):
        self.client.login(username='testuser', password='testpassword')
        new_booking = {'name': 'Alice Smith', 'booking_date': timezone.now(), 'no_of_guests': 3}
        response =  self.client.post(self.url_list, new_booking, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Booking.objects.filter(name='Alice Smith').exists())