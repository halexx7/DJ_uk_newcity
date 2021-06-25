import datetime
import json
from typing import KeysView
from dal import autocomplete

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core import serializers
from django.http import JsonResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from authnapp.models import User
from mainapp.models import (
    CurrentCounter,
    MainBook,
    Payment,
    PersonalAccountStatus,
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
    PrivilegesForm,
    PaymentsForm
    )


class UserPageCreate(LoginRequiredMixin, CreateView):
    model = User
    form_class = CurrentCounterForm
    context_object_name = "user"
    template_name = "personalacc/user_list.html"
    success_url = reverse_lazy("person:thanks")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profiles"] = UserProfile.objects.get(user=self.request.user)
        context["payments"] = MainBook.objects.filter(direction="C")
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
                data = self.get_form_kwargs()
                form = self.form_class(self.request.POST, initial=data['initial'])
        
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
        "subsidies_form": SubsidiesForm,
        "payments_form": PaymentsForm
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
        context["house_pay_debit"] = MainBook.get_all_debit()
        context["title"] = "Менеджер | ООО Новый город"
        return context

    def post(self, *args, **kwargs):
        post = self.request.POST
        user = self.request.POST.get("user")
        #TODO для проверки работы скрипта
        # period = datetime.datetime.now().date().replace(day=1, month=7)
        period = datetime.datetime.now().date().replace(day=1)
        handle = {
            "house_count_form": self.house_count_process,
            "recalculations_form": self.recalculations_process,
            "privilege_form": self.privilege_process,
            "subsidies_form": self.subsidies_process,
            "payments_form": self.payments_process
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
      
    def privilege_process(self, *args, **kwargs):
        update_values = {
            "sale": kwargs['post'].get("sale"),
            "desc": kwargs['post'].get('desc')
        }
        obj, created = Privileges.objects.update_or_create(
            user_id=kwargs['user'], service_id=kwargs['post'].get("service"), defaults=update_values
        )
        ser_instance = serializers.serialize("json", [obj,],)
        return ser_instance

    def subsidies_process(self, *args, **kwargs):
        update_values = {
            "sale": kwargs['post'].get("sale"),
            "desc": kwargs['post'].get('desc')
        }
        obj, created = Subsidies.objects.update_or_create(
            user_id=kwargs['user'], service_id=kwargs['post'].get("service"), defaults=update_values
        )
        ser_instance = serializers.serialize("json", [obj,],)
        return ser_instance

    def payments_process(self, *args, **kwargs):
        update_values = {
            "direction": kwargs['post'].get("direction"),
            "amount": kwargs['post'].get("amount")
        }
        obj, created = MainBook.objects.update_or_create(
            user_id=kwargs["user"], period=kwargs["period"], defaults=update_values
        )
        ser_instance = serializers.serialize("json", [obj,],)
        return ser_instance


class HouseHistoryListView(LoginRequiredMixin, ListView):
    model = HouseHistory
    context_object_name = "history"
    template_name = "personalacc/house_history_list.html"


class RecalcHistoryListView(LoginRequiredMixin, ListView):
    model = Recalculations
    context_object_name = "recalc"
    template_name = "personalacc/recalc_history_list.html"


class AccountsReceivableListView(LoginRequiredMixin, ListView):
    model = PersonalAccountStatus
    context_object_name = "receivable"
    template_name = "personalacc/accounts_receivable.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Дебиторская задолжность | ООО Новый город"
        context["appartament"] = Appartament.objects.all()
        return context


class UserAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor!
        if not self.request.user.is_authenticated:
            return User.objects.none()
        qs = User.objects.filter(is_staff=False)
        if self.q:
            qs = qs.filter(name__istartswith=self.q)
        return qs