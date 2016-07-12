from django.test import TestCase

from datetime import date
from .models import Vehicle

class VehicleViewTests(TestCase):
    def test_vehicle_list(self):
        response = self.client.get('/resources/vehicle_list/')
        self.assertEqual(response.status_code, 200)

    def test_must_create_vehicle(self):
        data = {
            "name": "Fiat Palio",
            "description": "Modelo popular, cor branca",
            "license_plate": "GMF5689",
            "manufacture_year": '2016-10-03'
        }
        response = self.client.post('/resources/vehicle/add/', data)
        #Check status code for redirect
        self.assertEqual(response.status_code, 302)
        veh_saved = Vehicle.objects.all().first()
        self.assertEqual(veh_saved.id, 1)
        self.assertEqual(veh_saved.name, 'Fiat Palio')


class VehicleTest(TestCase):

    def setUp(self):
        date_manufacture = date(2010, 1, 1)
        self.vehicle = Vehicle.objects.create(name='Uno', \
                license_plate='GMF7860', manufacture_year=date_manufacture)

    def test_models(self):
        self.assertTrue(self.vehicle.is_active)
        self.assertEqual(self.vehicle.usecontrols.count(), 0)
