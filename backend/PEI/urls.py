
from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^getProd/$', views.GetProducts),
    re_path(r'^getProd/(?P<id>[0-9])$', views.GetProduct),
    re_path(r'^getCart/$', views.GetCart),
    re_path(r'^addCart/(?P<id>[0-9])$', views.addCart),
    re_path(r'^rmCart/(?P<id>[0-9])$', views.rmCart),
]