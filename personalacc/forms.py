from django import forms
from mainapp.models import CurrentCounter
from crispy_forms.helper import FormHelper



class CurrentCounterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CurrentCounterForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
        self.helper = FormHelper()  
        self.helper.form_show_labels = False

    class Meta:
        model = CurrentCounter
        exclude = ("user", "created", "updated")
