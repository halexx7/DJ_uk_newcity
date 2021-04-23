import hashlib
import random

from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, UserChangeForm, UserCreationForm
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import Group
from django.forms import fields
from django.forms import models

from mainapp.models import Appartament, UserProfile
from .models import User

from django.forms.models import BaseInlineFormSet, inlineformset_factory
 
class BaseChildrenFormset(BaseInlineFormSet, forms.ModelForm):
    field_name = ["house", "number", "add_number",]

    def add_fields(self, form, index):
        super().add_fields(form, index)
        AppartamentFormset = inlineformset_factory(UserProfile, Appartament, fields=["gender",], extra=1)
 
        # save the formset in the 'nested' property
        form.nested = AppartamentFormset(
                        instance=form.instance,
                        data=form.data if form.is_bound else None,
                        files=form.files if form.is_bound else None,
                        prefix='appartament-%s-%s' % (
                            form.prefix,
                            AppartamentFormset.get_default_prefix()),
                        extra=1)
    
    class Meta:
        model = Appartament
        exclude = ()
 


class BootstrapStylesMixins:
    field_name = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.field_name:
            for fieldname in self.field_name:
                self.fields[fieldname].widget.attrs = {'class': 'form-control'}
        else:
            raise ValueError('The field_name should be set')


class UserLoginForm(BootstrapStylesMixins, AuthenticationForm):
    # В данном конкретном случае username = personal_account
    field_name = ["username", "password"]


class MyPasswordChangeForm(BootstrapStylesMixins, PasswordChangeForm):
    field_name = ["old_password", "new_password1", "new_password2"]


class MyPassResetForm(BootstrapStylesMixins, PasswordResetForm):
    field_name = ["email"]


class MyPassSetForm(BootstrapStylesMixins, SetPasswordForm):
    field_name = ["new_password1", "new_password2"]


class UserEditForm(BootstrapStylesMixins, UserChangeForm):
    field_name = ["name", "personal_account", "email", "phone"]

    class Meta:
        model = User
        fields = ("name", "personal_account", "email", "phone")


class AppartamentEditForm(BootstrapStylesMixins, forms.ModelForm):
    field_name = ["house", "number"]

    class Meta:
        model = Appartament
        fields = ("house", "number")


class UserProfileEditForm(BootstrapStylesMixins, forms.ModelForm):
    field_name = ["gender", "type_electric_meter"]

    class Meta:
        model = UserProfile
        fields = ("gender", "type_electric_meter")


class UserRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
            field.help_text = ""


    def save(self):
        user = super(UserRegisterForm, self).save()

        user.is_active = False
        user.groups.add(Group.objects.get(name="Client"))
        salt = hashlib.sha1(str(random.random()).encode("utf8")).hexdigest()[:6]
        user.activation_key = hashlib.sha1((user.email + salt).encode("utf8")).hexdigest()
        user.save()

        return user

    class Meta:
        model = User
        fields = ("personal_account", "name", "password1", "password2", "email")
