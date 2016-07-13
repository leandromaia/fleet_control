from django.contrib import admin

from .models import ManagerControl, Manufacturer, \
                            Vehicle, Driver, UseControl


@admin.register(ManagerControl)
class ManagerControlAdmin(admin.ModelAdmin):
    pass

@admin.register(Manufacturer)
class ManufacturerControlAdmin(admin.ModelAdmin):
    pass

@admin.register(Vehicle)
class VehicleControlAdmin(admin.ModelAdmin):
    pass

@admin.register(Driver)
class DriverControlAdmin(admin.ModelAdmin):
    pass

@admin.register(UseControl)
class UseControlControlAdmin(admin.ModelAdmin):
    pass
