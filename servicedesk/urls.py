from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^contact-me/$', views.contact, name='contact_me'),
    url(r'^thanks/$', TemplateView.as_view(template_name='thanks.html')),
]
