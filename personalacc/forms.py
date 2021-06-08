from crispy_forms.helper import FormHelper
from django import forms

from mainapp.models import CurrentCounter, HouseCurrent, HouseHistory, Recalculations


class CurrentCounterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
        self.helper = FormHelper()
        self.helper.form_show_labels = False

    class Meta:
        model = CurrentCounter
        exclude = ("col_water", "hot_water", "created", "updated")


class HomeCurrentCounterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
        self.helper = FormHelper()
        # self.helper.form_show_labels = False

    class Meta:
        model = HouseCurrent
        exclude = ("period", "created", "updated")


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
        super(RecalculationsForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
        self.helper = FormHelper()

    class Meta:
        model = Recalculations
        exclude = ("desc", "created", "updated")
