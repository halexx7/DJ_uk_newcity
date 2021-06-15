from django.contrib.auth.views import (
    PasswordChangeDoneView,
    PasswordChangeView,
    PasswordResetCompleteView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetView,
)
from django.urls import re_path
from django.urls.base import reverse, reverse_lazy

import authnapp.views as authnapp
from authnapp.apps import AuthnappConfig
from authnapp.views import ProfileUpdateView

from .forms import MyPassResetForm, MyPassSetForm, MyPasswordChangeForm

app_name = AuthnappConfig.name

urlpatterns = [
    re_path(r"^login/$", authnapp.login, name="login"),
    re_path(r"^logout/$", authnapp.logout, name="logout"),
    re_path(r"^register/$", authnapp.register, name="register"),
    re_path(r"^edit/(?P<pk>\d+)/$", ProfileUpdateView.as_view(), name="edit"),
    # re_path(r"^edit/$", authnapp.edit, name="edit"),
    re_path(r"^verify/(?P<email>.+)/(?P<activation_key>\w+)/$", authnapp.verify, name="verify"),
    # change password urls
    re_path(
        r"^password-change/$",
        PasswordChangeView.as_view(
            template_name="authnapp/password_change.html",
            success_url=reverse_lazy("auth:password_change_done"),
            form_class=MyPasswordChangeForm,
        ),
        name="password_change",
    ),
    re_path(
        r"^password-change/done/$",
        PasswordChangeDoneView.as_view(
            template_name="authnapp/password_change_done.html",
        ),
        name="password_change_done",
    ),
    # reset password urls
    re_path(
        r"^password-reset/$",
        PasswordResetView.as_view(
            template_name="authnapp/password_reset.html",
            email_template_name="authnapp/password_reset_email.html",
            success_url=reverse_lazy("auth:password_reset_done"),
            form_class=MyPassResetForm,
        ),
        name="password_reset",
    ),
    re_path(
        r"^password-reset/done/$",
        PasswordResetDoneView.as_view(
            template_name="authnapp/password_reset_done.html",
        ),
        name="password_reset_done",
    ),
    re_path(
        r"^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$",
        PasswordResetConfirmView.as_view(
            template_name="authnapp/password_reset_confirm.html",
            success_url=reverse_lazy("auth:password_reset_complete"),
            form_class=MyPassSetForm,
        ),
        name="password_reset_confirm",
    ),
    re_path(
        r"^password-reset/complete/$",
        PasswordResetCompleteView.as_view(
            template_name="authnapp/password_reset_complete.html",
        ),
        name="password_reset_complete",
    ),
]
