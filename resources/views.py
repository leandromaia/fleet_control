from datetime import date

from django.views.generic.base import RedirectView, TemplateView
from django.views.generic.edit import CreateView, \
                                UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render

from .models import Vehicle, Manufacturer, Driver, UseControl

def usecontrol_add(request):
    manufacturer = Manufacturer(name='Fiat')
    manufacturer.save()

    date_manufacture = date(2010, 1, 1)
    v1 = Vehicle(
            name='Uno',
            license_plate='HGM4567',
            manufacture_year=date_manufacture,
            manufacturer=manufacturer)
    v1.save()

    driver = Driver(name='Leandro Maia')
    driver.save()

    usecontrol = UseControl(driver=driver, vehicle=v1)
    usecontrol.save()
    return HttpResponse('Modelos criados com sucesso')

def usecontrol_list(request):
    #Busca o primeiro registro de UseControl
    usecontrol = UseControl.objects.all().first()
    data = {
        'vehicle': usecontrol.vehicle.name,
        'driver': usecontrol.driver.name,
        'date_started': usecontrol.date_started
    }
    import pdb; pdb.set_trace()
    return render(request, 'usecontrol_list.html', data)

class VehicleCreate(CreateView):
    model = Vehicle
    template_name = 'vehicle_form.html'
    fields = ['name', 'description', 'manufacture_year', 'license_plate']

class VehicleUpdate(UpdateView):
    model = Vehicle
    template_name = 'vehicle_form.html'
    fields = ['name']

class VehicleDelete(DeleteView):
    model = Vehicle
    success_url = reverse_lazy('vehicle_list')
    template_name = 'vehicle_confirm_delete.html'


class VehicleRedirectView(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'vehicle_detail'

    def get_redirect_url(self, *args, **kwargs):
        vehicle = get_object_or_404(Vehicle, pk=kwargs['pk'])
        return super(VehicleRedirectView, self).get_redirect_url(*args, **kwargs)


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['available_vehicles'] = Vehicle.objects.all()[:5]
        return context

class VehicleDetailView(DetailView):
    model = Vehicle
    template_name = 'vehicle_detail.html'

class VehicleListView(ListView):
    model = Vehicle
    template_name = 'list_vehicle.html'
    queryset = Vehicle.objects.order_by('name')
    context_object_name = 'vehicle_list'
    paginate_by = 2
