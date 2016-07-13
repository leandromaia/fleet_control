from datetime import date
from django.contrib import admin
from .models import ManagerControl, Manufacturer, \
                            Vehicle, Driver, UseControl

@admin.register(ManagerControl)
class ManagerControlAdmin(admin.ModelAdmin):
    pass

@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    pass

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('name', 'license_plate','year_format', 'is_active')
    list_display_links = ('name', 'license_plate')
    list_per_page = 2
    search_fields = ('name', 'description')
    list_filter = ('is_active', )

    def year_format(self, instance):
        return date.strftime(instance.manufacture_year, "%Y")
    year_format.short_description = 'Ano de Fabricação'

@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    pass

@admin.register(UseControl)
class UseControlAdmin(admin.ModelAdmin):
    pass
