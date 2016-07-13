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

class UseControlInline(admin.TabularInline):
    model = UseControl
    extra = 1

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    inlines = (UseControlInline,)
    fields = (('name', 'license_plate'),'manufacture_year')
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
     inlines = (UseControlInline,)
