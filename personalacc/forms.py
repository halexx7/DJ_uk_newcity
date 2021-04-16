from django import forms
from mainapp.models import CurrentCounter


class CurrentCounterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CurrentCounter, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"

    class Meta:
        model = CurrentCounter
        exclude = ("user", "created", "updated")
