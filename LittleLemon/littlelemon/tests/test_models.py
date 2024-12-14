from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=3, inventory=10)
        self.assertEqual(str(item), "IceCream : 3")