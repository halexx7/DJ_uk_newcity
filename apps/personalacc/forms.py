from crispy_forms.helper import FormHelper
from dal import autocomplete
from django import forms

from apps.authnapp.models import User
from apps.directory.models import Privileges, Services, Subsidies
from apps.mainapp.models import (CurrentCounter, HouseCurrent, HouseHistory,
                            MainBook, Recalculations)


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
        self.fields["user"].queryset = User.objects.filter(id=kwargs["initial"]["user"])
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
            if field_name == 'user':
                field.label = 'Лицевой счет'
                field.widget.attrs['readonly'] = True
                
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
    
    class Meta:
        model = Recalculations
        exclude = ('period', 'is_auto', 'created', 'updated', 'is_active')
     
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Отправляем фильтрованные данные в форму
        self.fields["service"].queryset = Services.objects.filter(const=False)
        
        for field_name, field in self.fields.items():            
            if field_name == 'user':
                field.label = 'Лицевой счет'
                field.widget = forms.TextInput()
                field.widget.attrs['id'] = 'personalaccInpRecalc'

            field.widget.attrs['class'] = 'form-control  field_form'
            field.help_text = ''


class SubsidiesForm(forms.ModelForm):
    class Meta:
        model = Privileges
        exclude = ('is_active', 'created', 'updated')
     
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Отправляем фильтрованные данные в форму
        self.fields["service"].queryset = Services.objects.filter(const=False)
        
        for field_name, field in self.fields.items():            
            if field_name == 'user':
                field.label = 'Лицевой счет'
                field.widget = forms.TextInput()
                field.widget.attrs['id'] = 'personalaccInpSubsidies'

            field.widget.attrs['class'] = 'form-control  field_form'


class PrivilegesForm(forms.ModelForm):
    
    class Meta:
        model = Privileges
        exclude = ('is_active', 'created', 'updated')
     
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Отправляем фильтрованные данные в форму
        self.fields["service"].queryset = Services.objects.filter(const=False)
        
        for field_name, field in self.fields.items():            
            if field_name == 'user':
                field.label = 'Лицевой счет'
                field.widget = forms.TextInput()
                field.widget.attrs['id'] = 'personalaccInpPrivileges'

            field.widget.attrs['class'] = 'form-control  field_form'


class PaymentsForm(forms.ModelForm):
    
    class Meta:
        model = MainBook
        exclude = ("created", "updated", "is_active")
     
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["direction"].queryset = MainBook.objects.all().filter(direction="D")
        
        for field_name, field in self.fields.items():
            if field_name == 'period':
                field.label = 'Период'
                field.widget.attrs['readonly'] = True
            
            if field_name == 'user':
                field.label = 'Лицевой счет'
                field.widget = forms.TextInput()
                field.widget.attrs['id'] = 'personalaccInpPayments'

            field.widget.attrs['class'] = 'form-control  field_form'
            field.help_text = ''
