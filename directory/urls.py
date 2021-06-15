from django.urls import re_path

import directory.views as directory
import personalacc.views as personalacc
from personalacc.apps import PersonalaccConfig

app_name = PersonalaccConfig.name

urlpatterns = [
    re_path(r"^$", directory.DirectoryList.as_view(), name="list"),
    # ServicesCategory
    re_path(r"^categories/create/$", directory.ServicesCategoryCreateView.as_view(), name="category_create"),
    re_path(
        r"^categories/update/(?P<pk>\d+)/$", directory.ServicesCategoryUpdateView.as_view(), name="category_update"
    ),
    re_path(
        r"^categories/delete/(?P<pk>\d+)/$", directory.ServicesCategoryDeleteView.as_view(), name="category_delete"
    ),
    # Services
    re_path(r"^services/create/category/(?P<pk>\d+)/$", directory.ServicesCreateView.as_view(), name="services_create"),
    re_path(r"^services/read/category/(?P<pk>\d+)/$", directory.ServicesListView.as_view(), name="services"),
    re_path(r"^services/update/(?P<pk>\d+)/$", directory.ServicesUpdateView.as_view(), name="services_update"),
    re_path(r"^services/delete/(?P<pk>\d+)/$", directory.ServicesDeleteView.as_view(), name="services_delete"),
    # City
    re_path(r"^city/create/$", directory.CityCreateView.as_view(), name="city_create"),
    re_path(r"^city/update/(?P<pk>\d+)/$", directory.CityUpdateView.as_view(), name="city_update"),
    re_path(r"^city/delete/(?P<pk>\d+)/$", directory.CityDeleteView.as_view(), name="city_delete"),
    # Street
    re_path(r"^street/create/city/(?P<pk>\d+)/$", directory.StreetCreateView.as_view(), name="street_create"),
    re_path(r"^street/read/city/(?P<pk>\d+)/$", directory.StreetListView.as_view(), name="streets"),
    re_path(r"^street/update/(?P<pk>\d+)/$", directory.StreetUpdateView.as_view(), name="street_update"),
    re_path(r"^street/delete/(?P<pk>\d+)/$", directory.StreetDeleteView.as_view(), name="street_delete"),
    # House
    re_path(r"^house/create/street/(?P<pk>\d+)/$", directory.HouseCreateView.as_view(), name="house_create"),
    re_path(r"^house/read/street/(?P<pk>\d+)/$", directory.HouseListView.as_view(), name="house"),
    re_path(r"^house/update/(?P<pk>\d+)/$", directory.HouseUpdateView.as_view(), name="house_update"),
    re_path(r"^house/delete/(?P<pk>\d+)/$", directory.HouseDeleteView.as_view(), name="house_delete"),
    # Appartaments
    re_path(
        r"^appartaments/create/house/(?P<pk>\d+)/$",
        directory.AppartamentsCreateView.as_view(),
        name="appartaments_create",
    ),
    re_path(r"^appartaments/read/house/(?P<pk>\d+)/$", directory.AppartamentsListView.as_view(), name="appartaments"),
    re_path(
        r"^appartaments/update/(?P<pk>\d+)/$", directory.AppartamentsUpdateView.as_view(), name="appartaments_update"
    ),
    re_path(
        r"^appartaments/delete/(?P<pk>\d+)/$", directory.AppartamentsDeleteView.as_view(), name="appartaments_delete"
    ),
    # Residents
    re_path(r"^resident/read/$", directory.ResidentsListView.as_view(), name="residents"),
    re_path(r"^resident/create/$", directory.ResidentsCreateView.as_view(), name="residents_create"),
    re_path(r"^resident/update/(?P<pk>\d+)/$", directory.ResidentsUpdateView.as_view(), name="residents_update"),
    re_path(r"^resident/delete/(?P<pk>\d+)/$", directory.ResidentsDeleteView.as_view(), name="residents_delete"),
]
