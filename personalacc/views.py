import datetime
import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core import serializers
from django.db import transaction
from django.db.models import F
from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver
from django.forms import inlineformset_factory
from django.http import JsonResponse, request
from django.shortcuts import HttpResponseRedirect, get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.views.generic.detail import DetailView

from authnapp.forms import UserEditForm, UserLoginForm, UserProfileEditForm, UserRegisterForm
from authnapp.models import User
from mainapp.models import (
    UK,
    Appartament,
    HistoryCounter,
    HouseCurrent,
    HouseHistory,
    Privileges,
    Recalculations,
    Subsidies,
    UserProfile,
)
from personalacc.forms import CurrentCounterForm, HomeCurrentCounterForm, HomeHistoryCounterForm, RecalculationsForm


# @login_required
def user(request):
    return render(request, "personalacc/user_acc.html")


# @login_required
def manager(request):
    return render(request, "personalacc/manager_acc.html")


class AjaxableResponseMixin(object):
    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.method == "POST" and self.request.is_ajax():
            data = {
                "pk": self.object.pk,
            }
            return JsonResponse(data)
        else:
            return response

    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response


class UserPageCreate(LoginRequiredMixin, CreateView):
    model = User
    form_class = CurrentCounterForm
    context_object_name = "user"
    template_name = "personalacc/user_list.html"
    success_url = reverse_lazy("person:user")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profiles"] = UserProfile.objects.filter(user=self.request.user)
        context["history"] = HistoryCounter.get_last_val(self.request.user)
        context["title"] = "Пользователь | ООО Новый город"
        return context


class ManagerPageCreate(LoginRequiredMixin, CreateView):
    form_class = HomeCurrentCounterForm
    first_form_class = HomeHistoryCounterForm
    second_form_class = RecalculationsForm
    template_name = "personalacc/manager_list.html"
    success_url = reverse_lazy("person:manager")

    def get_context_data(self, **kwargs):
        context = super(ManagerPageCreate, self).get_context_data(**kwargs)
        if "form" not in context:
            context["form"] = self.form_class()
        if "form2" not in context:
            context["form2"] = self.second_form_class()
        context["uk"] = UK.objects.all()
        context["house_history"] = HouseHistory.objects.all()
        context["house_current"] = HouseCurrent.objects.all()
        context["house_rec"] = Recalculations.objects.all()
        context["house_privileges"] = Privileges.objects.all()
        context["house_subsidies"] = Subsidies.objects.all()
        context["title"] = "Менеджер | ООО Новый город"
        return context

    def post(self, *args, **kwargs):
        if self.request.is_ajax and self.request.method == "POST":

            if self.request.POST.get("form_type") == "houseCounterForm":
                form = self.form_class(self.request.POST)
            elif self.request.POST.get("form_type") == "recalcForm":
                form = self.second_form_class(self.request.POST)

            if form.is_valid():
                post = self.request.POST
                house = post.get("house")
                period = datetime.datetime.now().date().replace(day=1)
                # period = datetime.datetime.now().date().replace(day=1, month=7)
                update_values = {
                    "col_water": post.get("col_water"),
                    "hot_water": post.get("hot_water"),
                    "electric_day": post.get("electric_day"),
                    "electric_night": post.get("electric_night"),
                }
                obj, created = HouseCurrent.objects.update_or_create(
                    house_id=house, period=period, defaults=update_values
                )
                # При создании новой записи удаляем старую
                if created:
                    previous_month = (period - datetime.timedelta(days=1)).replace(day=1)
                    previous_value = HouseCurrent.objects.filter(house_id=house, period=previous_month)
                    previous_value.delete()
                ser_instance = serializers.serialize(
                    "json",
                    [
                        obj,
                    ],
                )
                return JsonResponse({"instance": ser_instance}, status=200)
            else:
                return JsonResponse({"error": form.errors}, status=400)

        return JsonResponse({"error": ""}, status=400)


# При удалении ловим и сохраняем объект
@receiver(pre_delete, sender=HouseCurrent)
def copy_arhive_current_to_history_house(sender, instance, **kwargs):
    house = instance.house_id
    period = instance.period
    upd_val = {
        "col_water": instance.col_water,
        "hot_water": instance.hot_water,
        "electric_day": instance.electric_day,
        "electric_night": instance.electric_night,
    }
    obj, created = HouseHistory.objects.update_or_create(house_id=house, period=period, defaults=upd_val)


class HouseHistoryListView(LoginRequiredMixin, ListView):
    model = HouseHistory
    context_object_name = "history"
    template_name = "personalacc/house_history_list.html"
