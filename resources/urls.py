from django.conf.urls import url

from . import views
from .views import VehicleListView, VehicleDetailView

urlpatterns = [
    url(r'^list_vehicle/', VehicleListView.as_view()),
    url(r'^vehicle_view/(?P<pk>\d+)$', VehicleDetailView.as_view(), \
                                                name='vehicle_detail'),
    url(r'^$', views.index, name='index'),
]
