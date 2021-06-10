from crispy_forms.helper import FormHelper
from django import forms

from mainapp.models import CurrentCounter, HouseCurrent, HouseHistory, Privileges, Recalculations, Subsidies

class MultipleForm(forms.Form):
    """Добавляем клас Мульти формности, идентификация форм будет по скрытому полю action"""
    action = forms.CharField(max_length=60, widget=forms.HiddenInput())

class CurrentCounterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
        self.helper = FormHelper()
        self.helper.form_show_labels = False

    class Meta:
        model = CurrentCounter
        exclude = ("period", "electric_day", "electric_night", "electric_single", "created", "updated")


class HomeCurrentCounterForm(forms.ModelForm, MultipleForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
        self.helper = FormHelper()
        # self.helper.form_show_labels = False

    class Meta:
        model = HouseCurrent
        exclude = ("period", "created", "updated")


class HomeHistoryCounterForm(forms.ModelForm, MultipleForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
        self.helper = FormHelper()
        # self.helper.form_show_labels = False

    class Meta:
        model = HouseHistory
        exclude = ("period", "created", "updated")


class RecalculationsForm(forms.ModelForm, MultipleForm):
    def __init__(self, *args, **kwargs):
        super(RecalculationsForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
        self.helper = FormHelper()

    class Meta:
        model = Recalculations
        exclude = ("desc", "created", "updated")


class SubsidiesForm(forms.ModelForm, MultipleForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
        self.helper = FormHelper()

    class Meta:
        model = Subsidies
        exclude = ("desc", "created", "updated")


class PrivilegesForm(forms.ModelForm, MultipleForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
        self.helper = FormHelper()

    class Meta:
        model = Privileges
        exclude = ("desc", "created", "updated")