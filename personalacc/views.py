import datetime
import json
from typing import KeysView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core import serializers
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.http import JsonResponse
from django.shortcuts import HttpResponseRedirect, get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.views.generic.detail import DetailView

from authnapp.forms import UserEditForm, UserLoginForm, UserProfileEditForm, UserRegisterForm
from authnapp.models import User
from mainapp.models import (
    CurrentCounter,
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
from personalacc.forms import (
    CurrentCounterForm, 
    HomeCurrentCounterForm, 
    HomeHistoryCounterForm, 
    RecalculationsForm, 
    SubsidiesForm,
    PrivilegesForm
    )


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
    success_url = reverse_lazy("person:thanks")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profiles"] = UserProfile.objects.get(user=self.request.user)
        context["appartament"] = Appartament.objects.filter(user=self.request.user)
        context["history"] = HistoryCounter.get_last_val(self.request.user)
        context["title"] = "Пользователь | ООО Новый город"
        return context
    
    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super().get_form_kwargs(*args, **kwargs)
        #Заполняем форму начальными данными
        kwargs['initial'] = {'user': self.request.user.id}
        return kwargs
    

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.get(pk=self.request.user.id)


    def post(self, request, *args, **kwargs):
        if self.request.is_ajax and self.request.method == "POST":
            if self.request.POST.get("form_type") == "counterForm":
                form = self.form_class(self.request.POST)
        
            if form.is_valid():
                post = self.request.POST
                user = self.request.user
                # period = datetime.datetime.now().date().replace(day=1)
                #TODO для проверки работы скрипта
                period = datetime.datetime.now().date().replace(day=1, month=10)
                update_values = {
                    "col_water": post.get("col_water"),
                    "hot_water": post.get("hot_water"),
                    #TODO электричество пока отменяется
                    # "electric_day": post.get("electric_day"),
                    # "electric_night": post.get("electric_night"),
                }
                obj, created = CurrentCounter.objects.update_or_create(
                    user=user, period=period, defaults=update_values
                )
                # При создании новой записи удаляем старую
                if created:
                    previous_month = (period - datetime.timedelta(days=1)).replace(day=1)
                    previous_value = CurrentCounter.objects.filter(user=user, period=previous_month)
                    previous_value.delete()
                data = serializers.serialize("json", [obj,],)
                return JsonResponse({"instance": data}, status=200)
            else:
                return JsonResponse({"error": form.errors}, status=400)
        return JsonResponse({"error": ""}, status=400)


class ManagerPageCreate(LoginRequiredMixin, CreateView):
    form_class = HomeCurrentCounterForm
    form_classes = {
        "house_count_form": HomeCurrentCounterForm,
        "house_history_form": HomeHistoryCounterForm,
        "recalculations_form": RecalculationsForm,
        "privilege_form": PrivilegesForm,
        "subsidies_form": SubsidiesForm
        }
    template_name = "personalacc/manager_list.html"
    success_url = reverse_lazy("person:manager")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for name, form in self.form_classes.items():
            if name not in context:
                context[name] = form()
        context["uk"] = UK.objects.all()
        context["house_history"] = HouseHistory.objects.all()
        context["house_current"] = HouseCurrent.objects.all()
        context["house_rec"] = Recalculations.objects.all()
        context["house_privileges"] = Privileges.objects.all()
        context["house_subsidies"] = Subsidies.objects.all()
        context["title"] = "Менеджер | ООО Новый город"
        return context


    def post(self, *args, **kwargs):
        post = self.request.POST
        user = self.request.POST.get("user")
        period = datetime.datetime.now().date().replace(day=1)
        handle = {
            "house_count_form": self.house_count_process,
            "recalculations_form": self.recalculations_process,
            "privilege_form": self.privilege_process,
            "subsidies_form": self.subsidies_process
            }
        if self.request.is_ajax and self.request.method == "POST":
            type_form = post.get("form_type")

            for cls, el in self.form_classes.items():
                if type_form == cls:
                    form = el(post)
                    if form.is_valid():
                        func = handle[cls]
                        ser_instance = func(self, form=form, post=post, user=user, period=period)
                        return JsonResponse({"instance": ser_instance}, status=200)
                    else:
                        return JsonResponse({"error": form.errors}, status=400)
        return JsonResponse({"error": ""}, status=400)
    

    def house_count_process(self, *args, **kwargs):
        house = kwargs['post'].get("house")
        #TODO для проверки работы скрипта
        # period = datetime.datetime.now().date().replace(day=1, month=9)
        update_values = {
            "col_water": kwargs['post'].get("col_water"),
            "hot_water": kwargs['post'].get("hot_water"),
            #TODO электричество пока отменяется
            # "electric_day": post.get("electric_day"),
            # "electric_night": post.get("electric_night"),
        }
        obj, created = HouseCurrent.objects.update_or_create(
            house_id=house, period=kwargs['period'], defaults=update_values
        )
        # При создании новой записи удаляем старую
        if created:
            previous_month = (kwargs['period'] - datetime.timedelta(days=1)).replace(day=1)
            previous_value = HouseCurrent.objects.filter(house_id=house, period=previous_month)
            previous_value.delete()
        ser_instance = serializers.serialize("json", [obj,],)
        return ser_instance

    def recalculations_process(self, *args, **kwargs):
        update_values = {
            "recalc": kwargs['post'].get("recalc"),
            "desc": kwargs['post'].get("desc")
        }
        obj, created = Recalculations.objects.update_or_create(
            user_id=kwargs['user'], period=kwargs['period'], service_id=kwargs['post'].get("service"), defaults=update_values
        )
        ser_instance = serializers.serialize("json", [obj,],)
        return ser_instance
      
    def privilege_process(self, form, post, *args, **kwargs):
        update_values = {
            "sale": kwargs['post'].get("sale"),
            "desc": kwargs['post'].get('desc')
        }
        obj, created = Recalculations.objects.update_or_create(
            user_id=kwargs['user'], period=kwargs['period'], defaults=update_values
        )
        ser_instance = serializers.serialize("json", [obj,],)
        return ser_instance

    def subsidies_process(self, form, post, *args, **kwargs):
        post = self.request.POST
        user = post.get("user")
        period = datetime.datetime.now().date().replace(day=1)
        update_values = {
            "recalc": post.get("recalc"),
            "desc": post.get('desc')
        }
        obj, created = Recalculations.objects.update_or_create(
            user_id=user, period=period, defaults=update_values
        )
        ser_instance = serializers.serialize("json", [obj,],)
        return ser_instance


        

class HouseHistoryListView(LoginRequiredMixin, ListView):
    model = HouseHistory
    context_object_name = "history"
    template_name = "personalacc/house_history_list.html"


class ThanksListView(LoginRequiredMixin, ListView):
    model = User
    template_name = "personalacc/thanks.html"
