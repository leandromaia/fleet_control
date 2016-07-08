from django.db import models


class Vehicle(models.Model):

    name = models.CharField(max_length=30)
    description = models.TextField(null=True, blank=True)
    license_plate = models.CharField(max_length=7)
    manufacture_year = models.DateField()
    is_active = models.BooleanField(default=True)
