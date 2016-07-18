from django.test import TestCase
from resources.factories import DriverFactory

class DriverModelClass(TestCase):

    def setUp(self):
        self.driver_list = DriverFactory.create_batch(5)

    def test_driver_list(self):
        self.assertEqual(len(self.driver_list), 5)
