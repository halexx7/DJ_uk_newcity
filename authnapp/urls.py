from django.urls import re_path
from django.conf.urls import url


import authnapp.views as authnapp
from authnapp.views import passwordChange
from authnapp.apps import AuthnappConfig

app_name = AuthnappConfig.name

urlpatterns = [
    re_path(r"^login/$", authnapp.login, name="login"),
    re_path(r"^logout/$", authnapp.logout, name="logout"),
    re_path(r"^register/$", authnapp.register, name="register"),
    re_path(r"^edit/$", authnapp.edit, name="edit"),
    re_path(r"^verify/(?P<email>.+)/(?P<activation_key>\w+)/$", authnapp.verify, name="verify"),

    # change password urls
    re_path(r"^password-change/$", authnapp.passwordChange.as_view(), name='password_change'),
    re_path(r"^password-change/done/$", authnapp.passwordChangeDone.as_view(), name='password_change_done'),

#     re_path(r'^password-reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
#     re_path(r'^password-reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
#     re_path(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', 'django.contrib.auth.views.password_reset_confirm', name='password_reset_confirm'),
#     re_path(r'^password-reset/complete/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
]
