from datetime import date
import factory
from .models import Driver, Vehicle, Manufacturer
from factory.fuzzy import FuzzyDate

class DriverFactory(factory.DjangoModelFactory):
    class Meta:
         model = Driver
    name = factory.Sequence(lambda n: 'João {0}'.format(n))

class ManufacturerFactory(factory.DjangoModelFactory):
    class Meta:
         model = Manufacturer
    name = factory.Sequence(lambda n: 'Fabricante {0}'.format(n))

class VehicleFactory(factory.DjangoModelFactory):
    class Meta:
         model = Vehicle
    name = factory.Sequence(lambda n: 'João {0}'.format(n))
    manufacture_year = FuzzyDate(date(2008, 1, 1))
    manufacturer = factory.SubFactory(ManufacturerFactory)
