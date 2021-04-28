from django import forms

from mainapp.models import Appartament, City, House, Services, ServicesCategory, Street
from authnapp.forms import BootstrapStylesMixins

from django.forms.models import inlineformset_factory

 
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


class AppartamentsEditForm(BootstrapStylesMixins, forms.ModelForm):
    field_name = ["user", "house", "number", "add_number", "sq_appart", "num_owner", "is_active"]

    class Meta:
        model = Appartament
        fields = ("user", "house", "number", "add_number", "sq_appart", "num_owner", "is_active")


class AppartamentsInlineForm(BootstrapStylesMixins, forms.ModelForm):
    field_name = ["number", "add_number", "user", "sq_appart", "num_owner"]

    class Meta:
        model = Appartament
        fields = ("number", "add_number", "user", "sq_appart", "num_owner")


AppartamentFormset = inlineformset_factory(
    House,
    Appartament,
    form = AppartamentsInlineForm,
    extra=1,
    can_delete=False,
)