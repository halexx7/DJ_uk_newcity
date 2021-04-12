from django.urls import re_path

import personalacc.views as personalacc
from personalacc.apps import PersonalaccConfig

app_name = PersonalaccConfig.name

urlpatterns = [
    re_path(r"^user/$", personalacc.UserView.as_view(), name="user"),
    # re_path(r"^user/$", personalacc.user, name="user"),
    re_path(r"^manager/$", personalacc.manager, name="manager"),
]
