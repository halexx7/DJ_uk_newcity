import hashlib
import random

from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordChangeForm,
    PasswordResetForm,
    SetPasswordForm,
    UserChangeForm,
    UserCreationForm,
)
from django.contrib.auth.models import Group
from django.forms import fields, models
from django.forms.models import BaseInlineFormSet, inlineformset_factory

from mainapp.models import Appartament, UserProfile

from .models import User


class BootstrapStylesMixins:
    field_name = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.field_name:
            for fieldname in self.field_name:
                self.fields[fieldname].widget.attrs = {"class": "form-control"}
                if fieldname == "is_active" or fieldname == "const":
                    self.fields[fieldname].widget.attrs = {"class": "form_is-active"}
        else:
            raise ValueError("The field_name should be set")


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
        exclude = ("password",)


class AppartamentEditForm(BootstrapStylesMixins, forms.ModelForm):
    field_name = ["house", "number"]

    class Meta:
        model = Appartament
        fields = ("house", "number")


class UserProfileEditForm(BootstrapStylesMixins, forms.ModelForm):
    field_name = ["gender"]

    class Meta:
        model = UserProfile
        fields = ("gender",)


ProfileFormset = inlineformset_factory(
    User,
    UserProfile,
    form=UserProfileEditForm,
    extra=1,
    can_delete=False,
)


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


class AppartamentForm(BootstrapStylesMixins, forms.ModelForm):
    field_name = ["house", "number", "add_number"]

    class Meta:
        model = Appartament
        fields = ("house", "number", "add_number")


AppartamentFormset = inlineformset_factory(
    User,
    Appartament,
    form=AppartamentForm,
    extra=1,
    can_delete=False,
)