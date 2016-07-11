from django.conf.urls import url

from . import views
from .views import VehicleDetailView, VehicleRedirectView

urlpatterns = [
    url(r'^counter/(?P<pk>\d+)/$', VehicleRedirectView.as_view(), \
                                                name='vehicle_counter'),
    url(r'^vehicle_detail/(?P<pk>\d+)$', VehicleDetailView.as_view(), \
                                                name='vehicle_detail'),
]
