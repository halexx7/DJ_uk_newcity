from django.forms import widgets
from authnapp.models import User
from crispy_forms.helper import FormHelper
from django import forms
from dal import autocomplete

from authnapp.forms import BootstrapStylesMixins
from mainapp.models import CurrentCounter, HouseCurrent, HouseHistory, MainBook, Payment, Privileges, Recalculations, Services, Subsidies

class MultipleForm(forms.Form):
    """Добавляем клас Мульти формности, идентификация форм будет по скрытому полю action"""
    action = forms.CharField(max_length=60, widget=forms.HiddenInput())


class CurrentCounterForm(forms.ModelForm):
    class Meta:
        model = CurrentCounter
        exclude = ("period", "electric_day", "electric_night", "electric_single", "created", "updated")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['user'].queryset = User.objects.filter(id=kwargs['initial']['user'])
        self.fields['user'].queryset = User.objects.filter(id=kwargs['initial']['user'])
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
        self.helper = FormHelper()
        self.helper.form_show_labels = False


class HomeCurrentCounterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
        self.helper = FormHelper()
        self.helper.form_show_labels = False

    class Meta:
        model = HouseCurrent
        exclude = ("electric_day", "electric_night", "period", "created", "updated")


class HomeHistoryCounterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
        self.helper = FormHelper()
        # self.helper.form_show_labels = False

    class Meta:
        model = HouseHistory
        exclude = ("period", "created", "updated")


class RecalculationsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #Отправляем фильтрованные данные в форму
        self.fields['service'].queryset = Services.objects.filter(const=False)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
        self.helper = FormHelper()
        self.helper.form_show_labels = False

    class Meta:
        model = Recalculations
        exclude = ("period", "created", "updated")
        widgets = {
            "user": autocomplete.ModelSelect2(
                url="dal_user/",
                attrs={
                    "class": "form-control",
                    "data-pleaceholder": "Начните набирать имя жильца...",
                    "data-minimum-input-length": 3,
                },
            )
        }


class SubsidiesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['service'].queryset = Services.objects.filter(const=False)
        self.fields['user'].queryset = User.objects.none()
        self.helper = FormHelper()
        self.helper.form_show_labels = False

    class Meta:
        model = Subsidies
        exclude = ("created", "updated")
        widgets = {
        "user": autocomplete.ModelSelect2(
            url="dal_user/",
            attrs={
                "class": "form-control",
                "data-pleaceholder": "Начните набирать имя жильца...",
                "data-minimum-input-length": 3,
                },
            )
        }


class PrivilegesForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['service'].queryset = Services.objects.filter(const=False)
        self.fields['user'].queryset = User.objects.none()
        self.helper = FormHelper()
        self.helper.form_show_labels = False

    class Meta:
        model = Privileges
        exclude = ("is_active", "created", "updated")
        widgets = {
            "user": autocomplete.ModelSelect2(
                url="dal_user/",
                attrs={
                    "class": "form-control",
                    "data-pleaceholder": "Начните набирать имя жильца...",
                    "data-minimum-input-length": 3,
                },
            )
        }


class PaymentsForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['direction'].queryset = MainBook.objects.all().filter(direction="D")
        self.fields['user'].queryset = User.objects.none()
        self.helper = FormHelper()
        self.helper.form_show_labels = False

    class Meta:
        model = MainBook
        exclude = ("created", "updated")
        widgets = {
            "user": autocomplete.ModelSelect2(
                url="dal_user/",
                attrs={
                    "class": "form-control",
                    "data-pleaceholder": "Начните набирать имя жильца...",
                    "data-minimum-input-length": 3,
                },
            )
        }

    