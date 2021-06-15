from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column, Layout, Row, Submit
from django import forms
from django.forms.models import inlineformset_factory

from authnapp.admin import UserCreationForm
from authnapp.forms import BootstrapStylesMixins
from authnapp.models import User
from mainapp.models import Appartament, City, House, Services, ServicesCategory, Street


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
    field_name = ["city", "street", "is_active"]

    class Meta:
        model = Street
        fields = ("city", "street", "is_active")


class HouseEditForm(BootstrapStylesMixins, forms.ModelForm):
    field_name = ["city", "street", "number", "add_number", "sq_home", "uk", "category_rate", "is_active"]

    class Meta:
        model = House
        fields = ("city", "street", "number", "add_number", "sq_home", "uk", "category_rate", "is_active")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Column("city", css_class="form-group col-md-3 mb-0", lable="Город"),
                Column("street", css_class="form-group col-md-5 mb-0"),
                Column("number", css_class="form-group col-md-2 mb-0"),
                Column("add_number", css_class="form-group col-md-2 mb-0"),
                css_class="form-row",
            ),
            Row(
                Column("sq_home", css_class="form-group col-md-3 mb-0"),
                Column("uk", css_class="form-group col-md-5 mb-0"),
                Column("category_rate", css_class="form-group col-md-4 mb-0"),
                css_class="form-row",
            ),
            "is_active",
        )


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

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.form_tag = False
    #     self.helper.layout = Layout(
    #         'number',
    #         'add_number',
    #         'user',
    #         'sq_appart',
    #         'num_owner',
    #     )
    #     self.render_required_fields = True,
    #     self.helper.template = 'bootstrap4/table_inline_formset.html'


AppartamentFormSet = inlineformset_factory(
    House,
    Appartament,
    form=AppartamentsInlineForm,
    extra=1,
    can_delete=True,
)


class ResidentsEditForm(BootstrapStylesMixins, UserCreationForm):
    field_name = ["personal_account", "email"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "id-ResidentEditForm"
        self.helper.form_class = "blueForms"
        self.helper.form_method = "post"
        self.helper.form_action = "submit_survey"

        self.helper.add_input(
            Submit("submit", "Сохранить", css_class="form-control  bg-success  text-white  new_category_form--save")
        )
