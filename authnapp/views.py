from django.contrib import auth
from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse

from authnapp.forms import UserLoginForm


def login(request):
    title = "вход"

    login_form = UserLoginForm(data=request.POST or None)
    if request.method == "POST" and login_form.is_valid():
        personal_account = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(personal_account=personal_account, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse("invoice"))

    content = {"title": title, "login_form": login_form}
    return render(request, "authnapp/login.html", content)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse("invoice"))