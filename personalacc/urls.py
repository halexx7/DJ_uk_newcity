from django.urls import re_path

import personalacc.views as personalacc
from personalacc.apps import PersonalaccConfig

app_name = PersonalaccConfig.name

urlpatterns = [
    re_path(r"^user/$", personalacc.UserPageCreate.as_view(), name="user"),
    re_path(r"^manager/$", personalacc.ManagerPageCreate.as_view(), name="manager"),
    re_path(r"^manager/house_history/$", personalacc.HouseHistoryListView.as_view(), name="house_history"),
]
