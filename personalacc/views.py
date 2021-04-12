from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.db.models import F
from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver
from django.forms import inlineformset_factory
from django.http import JsonResponse
from django.shortcuts import HttpResponseRedirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.views.generic.detail import DetailView

from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse

from authnapp.forms import UserEditForm, UserLoginForm, UserProfileEditForm, UserRegisterForm
from authnapp.models import User
from mainapp.models import UserProfile

# @login_required
def user(request):
    return render(request, "personalacc/user_acc.html")

class UserView(ListView, LoginRequiredMixin):
    model = UserProfile
    context_object_name = 'user'
    template_name = 'personalacc/user_list.html'

    def get_queryset(self):
        return UserProfile.objects.filter(user=self.request.user)


# @login_required
def manager(request):
    return render(request, "personalacc/manager_acc.html")
    