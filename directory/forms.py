from django import forms

from mainapp.models import City, House, Services, ServicesCategory, Street
from authnapp.forms import BootstrapStylesMixins

 
class ServicesCategoryEditForm(BootstrapStylesMixins, forms.ModelForm):
    field_name = ["name", "is_active"]

    class Meta:
        model = ServicesCategory
        fields = ("name", "is_active")


class ServicesEditForm(BootstrapStylesMixins, forms.ModelForm):
    field_name = ["category", "name", "unit", "rate", "factor", "const", "is_active"]

    class Meta:
        model = Services
        fields = ("category", "name", "unit", "rate", "factor", "const", "is_active")
        

class CityEditForm(BootstrapStylesMixins, forms.ModelForm):
    field_name = ["city", "is_active"]

    class Meta:
        model = City
        fields = ("city", "is_active")


class StreetEditForm(BootstrapStylesMixins, forms.ModelForm):
    field_name = ["city", "street","is_active"]

    class Meta:
        model = Street
        fields = ("city", "street","is_active")


class HouseEditForm(BootstrapStylesMixins, forms.ModelForm):
    field_name = ["city", "street", "number", "add_number", "sq_home", "uk", "category_rate", "is_active"]

    class Meta:
        model = House
        fields = ("city", "street", "number", "add_number", "sq_home", "uk", "category_rate", "is_active")
