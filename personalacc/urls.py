from django.conf.urls import url
from django.urls import re_path

import personalacc.views as personalacc
from personalacc.apps import PersonalaccConfig

app_name = PersonalaccConfig.name

urlpatterns = [
    re_path(r"^user/$", personalacc.UserPageCreate.as_view(), name="user"),

    re_path(r"^manager/dal_user/$", personalacc.UserAutocomplete.as_view(), name="dal_user"),
    re_path(r"^manager/$", personalacc.ManagerPageCreate.as_view(), name="manager"),
    re_path(r"^manager/house_history/$", personalacc.HouseHistoryListView.as_view(), name="house_history"),
    re_path(r"^manager/recalc_history/$", personalacc.RecalcHistoryListView.as_view(), name="recalc_history"),
    re_path(r"^manager/receivable/$", personalacc.AccountsReceivableListView.as_view(), name="receivable"),

]

