import datetime
import decimal
import json

from django.conf import settings
from django.contrib.postgres import fields
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.core.serializers import serialize
from django.shortcuts import get_object_or_404, render
from django.utils.safestring import mark_safe
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.views.generic.detail import DetailView

from authnapp.models import User
from mainapp.models import (
    UK,
    Appartament,
    City,
    ConstantPayments,
    CurrentCounter,
    HistoryCounter,
    House,
    HouseCurrent,
    HouseHistory,
    Metrics,
    Payment,
    PersonalAccountStatus,
    Privileges,
    Profit,
    Recalculations,
    Services,
    ServicesCategory,
    Standart,
    Street,
    Subsidies,
    UserProfile,
    VariablePayments,
)


def main(request):

    invoice = mark_safe(serialize("json", User.objects.filter(pk=1)))
    return render(request, "invoice/main.html", context={"data": invoice})


# class InvoiceViews(ListView):
#     model = User

#     def get_context_data(self, **kwargs):
#         pass


class InvoiceViews(ListView):
    context_object_name = "user"
    template_name = "invoice/main.html"
    queryset = mark_safe(serialize("json", User.objects.filter(pk=1)))

    def get_context_data(self, **kwargs):
        # get_calc_const()
        # get_calc_variable()
        context = super(InvoiceViews, self).get_context_data(**kwargs)
        context["const"] = mark_safe(serialize("json", ConstantPayments.objects.filter(id=1)))
        context["hist"] = mark_safe(serialize("json", HistoryCounter.get_last_val(1)))
        context["curr"] = mark_safe(serialize("json", CurrentCounter.get_last_val(1)))
        context["appartaments"] = mark_safe(serialize("json", Appartament.objects.all()))
        context["house"] = mark_safe(serialize("json", House.objects.all()))
        context["city"] = mark_safe(serialize("json", City.objects.all()))
        context["street"] = mark_safe(serialize("json", Street.objects.all()))
        context["uk"] = mark_safe(serialize("json", UK.objects.all()))
        context["variable"] = mark_safe(
            serialize("json", VariablePayments.objects.filter(user_id=1).distinct("service"))
        )
        return context


# Расчет КОНСТАНТНЫХ платежей (по сигналу)
def get_calc_const():
    users = User.objects.select_related()
    rate = Services.get_const_payments(1)

    for user in users:
        data = []
        total = 0
        for el in rate:
            element = dict()
            element["service"] = el.name
            element["unit"] = el.unit
            element["rate"] = el.rate

            if el.unit == "м2":
                element["accured"] = el.rate * user.appartament.sq_appart
            elif el.unit == "чел":
                element["accured"] = el.rate * user.appartament.num_owner
            else:
                element["accured"] = el.rate

            element["standart"] = ""
            element["volume"] = ""
            element["coefficient"] = el.factor if el.factor >= 0 else ""
            element["subsidies"] = ""
            element["privileges"] = ""
            element["recalculations"] = ""
            element["total"] = element["accured"]

            data.append(element)
        user_id = User.objects.get(id=user.id)
        record = ConstantPayments(user=user_id, data=json.dumps(data, ensure_ascii=False, default=str))
        record.save()
    return data


# Расчет ПЕРЕМЕННЫХ платежей (по сигналу)
def get_calc_variable():
    users = User.objects.select_related()
    curr = CurrentCounter.objects.get(id=1)
    hist = HistoryCounter.get_last_val(1)[0]
    rate = Services.get_varybose_payments(1)
    subs = Subsidies.objects.select_related()
    priv = Privileges.objects.select_related()

    for user in users:
        user_id = User.objects.get(id=user.id)
        # Канализация (водоотведение)
        sewage = 0

        for el in rate:
            standart = el.standart
            if el.name == "Холодная вода (индивидуальное потребление)":
                accured = el.rate * (curr.col_water - hist.hist_col_water)
                sewage += accured
            elif el.name == "Горячая вода (индивидуальное потребление)":
                accured = el.rate * (curr.hot_water - hist.hist_hot_water)
                sewage += accured
            elif el.name == "Электроэнергия день":
                accured = el.rate * (curr.electric_day - hist.hist_electric_day)
            elif el.name == "Электроэнергия ночь":
                accured = el.rate * (curr.electric_night - hist.hist_electric_night)
            coefficient = el.factor if el.factor > 0 else 1
            subsidies = get_sale(el.name, subs)
            privileges = get_sale(el.name, priv)

            # Заменить на значение
            recalculations = 0

            total = (accured * coefficient) * decimal.Decimal(1 - (subsidies + privileges) / 100) - recalculations

            record = VariablePayments(
                user=user_id,
                # TODO Попробуем данный тип представления даты
                period=datetime.datetime.today().strftime("%Y/%m/%d"),
                service=el.name,
                unit=el.unit,
                standart=standart,
                volume=(curr.hot_water - hist.hist_hot_water) if (curr.hot_water - hist.hist_hot_water) > 0 else 0,
                rate=el.rate,
                accured=accured,
                coefficient=coefficient,
                subsidies=subsidies,
                privileges=privileges,
                recalculations=recalculations,
                total=total,
            )
            record.save()


# Возваращает субсидию или льготу при наличии
def get_sale(name, arr):
    for el in arr:
        if el.service.name == name:
            return el.sale
        else:
            return 0
