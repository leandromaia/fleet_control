from django.conf.urls import url

from . import views
from .views import VehicleListView

urlpatterns = [
    url(r'^list_vehicle/', VehicleListView.as_view()),
    url(r'^$', views.index, name='index'),
]
