from django.urls import re_path

import personalacc.views as personalacc
import directory.views as directory
from personalacc.apps import PersonalaccConfig

app_name = PersonalaccConfig.name

urlpatterns = [
    re_path(r"^$", directory.DirectoryList.as_view(), name='list'),

    #ServicesCategory
    re_path(r"^categories/create/$", directory.ServicesCategoryCreateView.as_view(), name="category_create"),
    re_path(r"^categories/update/(?P<pk>\d+)/$", directory.ServicesCategoryUpdateView.as_view(), name="category_update"),
    re_path(r"^categories/delete/(?P<pk>\d+)/$", directory.ServicesCategoryDeleteView.as_view(), name="category_delete"),

    #Services
    re_path(r"^services/create/category/(?P<pk>\d+)/$", directory.ServicesCreateView.as_view(), name="services_create"),
    re_path(r"^services/read/category/(?P<pk>\d+)/$", directory.ServicesListView.as_view(), name="services"),
    re_path(r"^services/update/(?P<pk>\d+)/$", directory.ServicesUpdateView.as_view(), name="services_update"),
    re_path(r"^services/delete/(?P<pk>\d+)/$", directory.ServicesDeleteView.as_view(), name="services_delete"),

    #City
    re_path(r"^city/create/$", directory.CityCreateView.as_view(), name="city_create"),
    re_path(r"^city/update/(?P<pk>\d+)/$", directory.CityUpdateView.as_view(), name="city_update"),
    re_path(r"^city/delete/(?P<pk>\d+)/$", directory.CityDeleteView.as_view(), name="city_delete"),

    #Street
    re_path(r"^street/create/city/(?P<pk>\d+)/$", directory.StreetCreateView.as_view(), name="street_create"),
    re_path(r"^street/read/city/(?P<pk>\d+)/$", directory.StreetListView.as_view(), name="streets"),
    re_path(r"^street/update/(?P<pk>\d+)/$", directory.StreetUpdateView.as_view(), name="street_update"),
    re_path(r"^street/delete/(?P<pk>\d+)/$", directory.StreetDeleteView.as_view(), name="street_delete"),
]
