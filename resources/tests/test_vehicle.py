from datetime import date

from django.test import TestCase
from django.core.urlresolvers import reverse

from resources.models import Vehicle, Manufacturer


class VehicleTests(TestCase):

    def setUp(self):
        manufacturer = Manufacturer(name='Fiat Company')
        manufacturer.save()
        year_manufacture = date(2007, 1, 1)
        self.vehicle = Vehicle(
            name='Uno', license_plate='WRF8900', \
            manufacture_year=year_manufacture, manufacturer=manufacturer
        )
        self.vehicle.save()

    def test_vehicle_is_active_must_be_true(self):
        self.assertTrue(self.vehicle.is_active)


class VehicleViewTests(TestCase):
    fixtures = ['vehicle_fixture']
    def setUp(self):
        self.manufacturer = Manufacturer.objects.create(name='Fiat')

    def test_fixture_value(self):
        vehicle = Vehicle.objects.get(pk=1)
        self.assertEqual(vehicle.name, 'Uno')
        self.assertEqual(vehicle.manufacturer.name, 'Fiat')


    def test_must_create_vehicle(self):
        data = {
            'name': 'Uno Fire',
            'description': 'Carro bão',
            'license_plate': 'GGM8976',
            'manufacture_year': '2007-01-01',
            'manufacturer': self.manufacturer.id
        }
        url = reverse('vehicle_add')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        veh_saved = Vehicle.objects.all().first()
        self.assertEqual(veh_saved.id, 2)
        self.assertEqual(veh_saved.name, 'Uno Fire')

class VehicleUpdateViewTests(TestCase):
    fixtures= ['vehicle_fixture']

    def test_must_update_vehicle_by_view(self):
        data = {
            'name': 'Uno Fire',
            'description': 'Carro bao',
            'license_plate': 'GGE0098',
            'manufacture_year': '2007-01-01',
            'manufacturer': 1
        }
        url = reverse('vehicle_update', kwargs={'pk': 1})
        response = self.client.post(url, data)
        vehicle = Vehicle.objects.get(pk=1)
        self.assertEqual(vehicle.name, 'Uno Fire')


class VehicleDeleteViewTests(TestCase):
    fixtures= ['vehicle_fixture']

    def test_must_delete_vehicle_by_view(self):
        url = reverse('vehicle_delete', kwargs={'pk': 1})
        response = self.client.post(url)
        vehicle_list = Vehicle.objects.all()
        self.assertRaises(Vehicle.DoesNotExist, Vehicle.objects.get, pk=1)
