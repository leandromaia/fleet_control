from django.views.generic import ListView

from .models import Vehicle


class VehicleListView(ListView):
    model = Vehicle
    template_name = 'list_vehicle.html'
    queryset = Vehicle.objects.order_by('name')
    context_object_name = 'vehicle_list'
    paginate_by = 2


from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    variables = {
        'course_name': 'Python e Django na Pratica',
        'alunos_list':[
            {
                'name': 'José34'
            },
            {
                'name': 'Maria'
            },
            {
                'name': 'João'
            }
        ]
    }

    return render(request, "hello.html", variables)
