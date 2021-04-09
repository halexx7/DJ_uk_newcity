from django.urls import path

import authnapp.views as authnapp

app_name = "authnapp"

urlpatterns = [
    path("login/", authnapp.login, name="login"),
    path("logout/", authnapp.logout, name="logout"),
]