from django.db import models
from django.conf import settings


class ManagerControl(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True)
    name = models.CharField(max_length=30)


class Manufacturer(models.Model):
    name = models.CharField(max_length=30, unique=True)


class Vehicle(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(null=True, blank=True)
    license_plate = models.CharField(max_length=7)
    manufacture_year = models.DateField()
    is_active = models.BooleanField(default=True)
    usecontrols = models.ManyToManyField('Driver', through='UseControl')


class Driver(models.Model):
    name = models.CharField(max_length=128)


class UseControl(models.Model):
    driver = models.ForeignKey(Driver)
    vehicle = models.ForeignKey(Vehicle)
    date_started = models.DateTimeField(auto_now_add=True)
    date_ended = models.DateTimeField(blank=True, null=True)
