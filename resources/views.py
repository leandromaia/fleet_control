from django.views.generic.base import TemplateView
from django.views.generic.base import RedirectView
from .models import Vehicle



class VehicleRedirectView(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'vehicle_detail'

    def get_redirect_url(self, *args, **kwargs):
        vehicle = get_object_or_404(Vehicle, pk=kwargs['pk'])
        vehicle.update_counter()
        return super(VehicleRedirectView, self).get_redirect_url(*args, **kwargs)


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['available_vehicles'] = Vehicle.objects.all()[:5]
        return context







from django.views.generic import ListView, DetailView

from .models import Vehicle


class VehicleDetailView(DetailView):
    model = Vehicle
    template_name = 'vehicle_detail.html'


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
