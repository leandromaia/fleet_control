from django import template

register = template.Library()

@register.simple_tag
def get_vehicles(number_items):
    list_vehicle = list()
    list_vehicle.append('Uno')
    list_vehicle.append('Palio')
    list_vehicle.append('Sandero')
    list_vehicle.append('Onix')
    list_vehicle.append('Tornado')
    list_vehicle.append('Mercedes C180')
    list_vehicle.append('Corola')

    return list_vehicle[:number_items]
