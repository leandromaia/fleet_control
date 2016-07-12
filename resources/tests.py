from datetime import date

from django.test import TestCase

from .models import Vehicle

class VehicleTest(TestCase):

    def setUp(self):
        date_manufacture = date(2010, 1, 1)
        self.vehicle = Vehicle.objects.create(name='Uno', \
                license_plate='GMF7860', manufacture_year=date_manufacture)

    def test_models(self):
        self.assertTrue(self.vehicle.is_active)
        self.assertEqual(self.vehicle.usecontrols.count(), 0)


class VehicleViewTests(TestCase):
    def test_vehicle_list(self):
        response = self.client.get('/resources/vehicle_list/')
        self.assertEqual(response.status_code, 200)
