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
from personalacc.forms import CurrentCounterForm

# @login_required
def user(request):
    return render(request, "personalacc/user_acc.html")

# class UserView(ListView, LoginRequiredMixin):
#     model = User
#     context_object_name = 'user'
#     template_name = 'personalacc/user_list.html'

#     def get_queryset(self):
#         return User.objects.filter(id=self.request.user.id)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         profiles = UserProfile.objects.filter(user=self.request.user)
#         context['profiles'] = profiles
#         return context

    


# @login_required
def manager(request):
    return render(request, "personalacc/manager_acc.html")
    

class UserPageCreate(LoginRequiredMixin, CreateView):
    model = User
    form_class = CurrentCounterForm
    context_object_name = 'user'
    template_name = 'personalacc/user_list.html'
    success_url = reverse_lazy('person:user')

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)

    def get_context_data(self, **kwargs):
        context = super(UserPageCreate, self).get_context_data(**kwargs)
        profiles = UserProfile.objects.filter(user=self.request.user)
        context['profiles'] = profiles
        context['title'] = 'Test'
        return context