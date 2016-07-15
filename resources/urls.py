from django.conf.urls import url
from . import views
from .views import VehicleCreate, VehicleUpdate, VehicleDelete, \
                    VehicleDetailView, VehicleRedirectView, VehicleListView

urlpatterns = [
    url(r'vehicle/add/$', VehicleCreate.as_view(), name='vehicle_add'),
    url(r'vehicle/(?P<pk>\d+)/$', VehicleUpdate.as_view(), \
                                                name='vehicle_update'),
    url(r'vehicle/(?P<pk>\d+)/delete/$', VehicleDelete.as_view(), \
                                                name='vehicle_delete'),
    url(r'^vehicle_detail/(?P<pk>\d+)$', VehicleDetailView.as_view(), \
                                                name='vehicle_detail'),
    url(r'^validate_vehicle/(?P<pk>\d+)/$', VehicleRedirectView.as_view(), \
                                                name='vehicle_detail'),
    url(r'^vehicle_list/$', VehicleListView.as_view(), \
                                                name='vehicle_list'),

    url(r'usecontrol/add/$', views.usecontrol_add, name='usecontrol_add'),
    url(r'usecontrol/list/$', views.usecontrol_list, name='usecontrol_list'),
]
