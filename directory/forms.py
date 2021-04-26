from django import forms

from mainapp.models import Services, ServicesCategory
from authnapp.forms import BootstrapStylesMixins

 
class ProductCategoryEditForm(BootstrapStylesMixins, forms.ModelForm):
    field_name = ["name", "is_active"]

    class Meta:
        model = ServicesCategory
        fields = ("name", "is_active")


class ProductEditForm(BootstrapStylesMixins, forms.ModelForm):
    field_name = ["category", "name", "unit", "rate", "factor", "const", "is_active"]

    class Meta:
        model = Services
        fields = ("category", "name", "unit", "rate", "factor", "const", "is_active")
        