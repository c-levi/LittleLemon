from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.item1 = Menu.objects.create(title="IceCream", price=3, inventory=10)
        self.item2 = Menu.objects.create(title="Pasta", price=12.5, inventory=4)
        self.item3 = Menu.objects.create(title="Fish", price=15, inventory=1)

    def test_getall(self):
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)

        expected_data = [
            {'id': self.item1.id, 'title': 'IceCream', 'price': '3.00', 'inventory': 10},
            {'id': self.item2.id, 'title': 'Pasta', 'price': '12.50', 'inventory': 4},
            {'id': self.item3.id, 'title': 'Fish', 'price': '15.00', 'inventory': 1},
        ]

        self.assertEqual(serializer.data, expected_data)