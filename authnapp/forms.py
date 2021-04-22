import hashlib
import random

from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, UserChangeForm, UserCreationForm
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import Group
from django.forms import fields

from mainapp.models import UserProfile

from .models import User


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


class UserEditForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
            field.help_text = ""

    def clean_age(self):
        data = self.cleaned_data["age"]
        if data < 18:
            raise forms.ValidationError("Вы слишком молоды!")

        return data

    class Meta:
        model = User
        fields = ("personal_account", "name", "email")


class UserProfileEditForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ("appartament", "type_electric_meter")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"



