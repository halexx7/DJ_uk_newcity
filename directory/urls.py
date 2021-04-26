from django.urls import re_path

import personalacc.views as personalacc
import directory.views as directory
from personalacc.apps import PersonalaccConfig

app_name = PersonalaccConfig.name

urlpatterns = [
    re_path(r"^$", directory.DirectoryList.as_view(), name='list'),
    # re_path(r"^city/read/$", directory.CityListView.as_view(), name="cities"),
    # re_path(r"^city/create/$", directory.CityCreateView.as_view(), name="city_cteate"),
    # re_path(r"^city/update/(?P<pk>\d+)/$", directory.CityUpdateView.as_view(), name="city_update"),
    # re_path(r"^city/delete/(?P<pk>\d+)/$", directory.CityDeleteView.as_view(), name="city_delete"),

    #ServicesCategory
    re_path(r"^categories/create/$", directory.ServicesCategoryCreateView.as_view(), name="category_create"),
    re_path(r"^categories/update/(?P<pk>\d+)/$", directory.ProductCategoryUpdateView.as_view(), name="category_update"),
    re_path(r"^categories/delete/(?P<pk>\d+)/$", directory.ProductCategoryDeleteView.as_view(), name="category_delete"),

    #Services
    re_path(r"^services/create/category/(?P<pk>\d+)/$", directory.ServicesCreateView.as_view(), name="services_create"),
    re_path(r"^services/read/category/(?P<pk>\d+)/$", directory.ServicesListView.as_view(), name="services"),
    re_path(r"^services/read/(?P<pk>\d+)/$", directory.ServicesDetailView.as_view(), name="services_read"),
    re_path(r"^services/update/(?P<pk>\d+)/$", directory.ServicesUpdateView.as_view(), name="services_update"),
    re_path(r"^services/delete/(?P<pk>\d+)/$", directory.ServicesDeleteView.as_view(), name="services_delete"),
]
