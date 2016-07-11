from django.views.generic.base import RedirectView, TemplateView
from django.views.generic.edit import CreateView, \
                                UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.core.urlresolvers import reverse_lazy
from .models import Vehicle

class VehicleCreate(CreateView):
    model = Vehicle
    template_name = 'vehicle_form.html'
    fields = ['name']

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
