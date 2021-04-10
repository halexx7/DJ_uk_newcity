from django.conf import settings
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse

from authnapp.forms import UserEditForm, UserLoginForm, UserProfileEditForm, UserRegisterForm
from authnapp.models import User


def user(request):
    return render(request, "personalacc/user_acc.html")


def manager(request):
    return render(request, "personalacc/manager_acc.html")
    