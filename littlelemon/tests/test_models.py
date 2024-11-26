from django.test import TestCase
from restaurant.models import Menu, Booking
from decimal import Decimal
from datetime import datetime
from django.utils.timezone import make_aware

class MenuTest(TestCase):
    def setUp(self) -> None:
        self.item1 = Menu.objects.create(title = 'Pizza', price = Decimal('12.99'), inventory = 10)
        
    def test_create_menu_item(self) -> None:
        item2 = Menu.objects.create(title = 'Burger', price = Decimal('17.99'), inventory = 5)
        self.assertEqual(Menu.objects.count(), 2)
        self.assertEqual(item2.title, 'Burger')
        self.assertEqual(item2.price, Decimal('17.99'))
        self.assertEqual(item2.inventory, 5)
        
    def test_get_menu_item(self) -> None:
        item  = Menu.objects.get(id = self.item1.id)
        self.assertEqual(item.title, 'Pizza')
        self.assertEqual(item.price, Decimal('12.99').quantize(Decimal('0.00')))
        self.assertEqual(item.inventory, 10)
        
    def test_delete_menu_item(self) -> None:
        item = Menu.objects.get(id=self.item1.id)
        item.delete()
        self.assertEqual(Menu.objects.count(), 0)

class BookingTest(TestCase):
    def setUp(self) -> None:
        self.booking1 = Booking.objects.create(name = "John Doe", no_of_guests = 3, booking_date = make_aware(datetime(2024, 11, 25, 18, 30)))
    
    def test_create_booking(self) -> None:
        booking2 = Booking.objects.create(name = "Jane Smith", no_of_guests = 2, booking_date = make_aware(datetime(2024, 12, 1, 20, 0)))
        self.assertEqual(Booking.objects.count(), 2)
        self.assertEqual(booking2.name, "Jane Smith")
        self.assertEqual(booking2.no_of_guests, 2)
        self.assertEqual(booking2.booking_date, make_aware(datetime(2024, 12, 1, 20, 0)))
        
    def test_get_booking(self) -> None:
        booking = Booking.objects.get(id = self.booking1.id)
        self.assertEqual(booking.name, "John Doe")
        self.assertEqual(booking.no_of_guests, 3)
        self.assertEqual(booking.booking_date, make_aware(datetime(2024, 11, 25, 18, 30)))
        
    def test_delete_booking(self) -> None:
        booking = Booking.objects.get(id = self.booking1.id)
        booking.delete()
        self.assertEqual(Booking.objects.count(), 0)
        
    def test_str_representation(self) -> None:
        self.assertEqual(str(self.booking1), "John Doe")