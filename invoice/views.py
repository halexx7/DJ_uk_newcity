import datetime
import decimal
import json
import re

from django.core.serializers import serialize
from django.utils.safestring import mark_safe
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from authnapp.models import User
from mainapp.models import (
    HeaderData,
    UK,
    Appartament,
    ConstantPayments,
    CurrentCounter,
    HistoryCounter,
    PersonalAccountStatus,
    Privileges,
    Recalculations,
    Services,
    Standart,
    Subsidies,
    VariablePayments,
)


def main(request):
    pass


class InvoiceViews(ListView):
    model = User
    context_object_name = "user"
    template_name = "invoice/invoice.html"

    def get_queryset(self):
        return User.objects.filter(pk = self.request.user.id)

    def get_context_data(self, **kwargs):
        user = self.request.user
        self.wrapper()
        context = super().get_context_data(**kwargs)
        context["header"] = mark_safe(serialize("json", HeaderData.objects.filter(user=user)))
        context["constant"] = mark_safe(serialize("json", ConstantPayments.objects.filter(user=user)))
        context["variable"] = mark_safe(serialize("json", VariablePayments.get_last_val(user.id)))
        context["status"] = mark_safe(serialize("json", PersonalAccountStatus.get_item(user)))
        return context

    def wrapper(self):
        get_calc_const()
        get_calc_variable()
        get_head_data()
    

# Расчет КОНСТАНТНЫХ платежей (по сигналу когда идут изменения в таблице Services)
def get_calc_const():
    users = User.objects.select_related().filter(is_staff=False)
    rate = Services.get_const_payments(1)

    for user in users:
        data = []
        total = 0
        pre_total = 0

        user_id = User.objects.get(id=user.id)
        appart = Appartament.objects.get(user=user)
        for el in rate:
            element = dict()
            element["service"] = el.name
            element["unit"] = el.unit
            element["rate"] = el.rate

            if el.unit.name == "м2":
                element["accured"] = el.rate * appart.sq_appart
            elif el.unit.name == "чел":
                element["accured"] = el.rate * appart.num_owner
            else:
                element["accured"] = el.rate

            element["standart"] = ""
            element["volume"] = ""
            element["coefficient"] = el.factor if el.factor >= 0 else ""
            element["subsidies"] = 0
            element["privileges"] = 0
            element["recalculation"] = 0
            element["total"] = element["accured"]
            element["pre_total"] = element["accured"]
            pre_total += element["pre_total"]
            total += element["total"]

            data.append(element)

        update_values = {
            "data": json.dumps(data, ensure_ascii=False, default=str),
            "total": decimal.Decimal(total),
            "pre_total": decimal.Decimal(total)
        }
        obj, created = ConstantPayments.objects.update_or_create(
            user=user_id, defaults=update_values
        )
    return (data, total)

# Расчет ПЕРЕМЕННЫХ платежей (по сигналу)
#TODO Какой сигнал? 30 число? или же после внесения счетчиков?
def get_calc_variable():
    users = User.objects.filter(is_staff=False)
    rate = Services.get_varybose_payments(1)

    for user in users:
        data = []
        total = 0 
        pre_total = 0
        period = datetime.datetime.now().replace(day=1)
        user_id = User.objects.get(id=user.id)
        appa = Appartament.get_item(user.id)[0]
        stand = Standart.get_last_val(appa.house_id)[0]
        sq_appa = appa.sq_appart
        hist = HistoryCounter.get_last_val(user.id)[0]

        try:
            #Если счетчики введены, считаем объем
            object_curr = CurrentCounter.get_last_val(user.id)[0]
            #TODO Почему тип list???
            volume_col = object_curr.col_water - hist.col_water,
            volume_hot = object_curr.hot_water - hist.hot_water,
            volume_sewage = volume_col[0] + volume_hot[0]
            curr = {
                "standart": False, 
                "volume_col": volume_col[0], 
                "volume_hot": volume_hot[0],
                "volume_sewage": volume_sewage,
                "period": object_curr.period
                }
        except:
            #Если счетчики не введены, берем общедомовой средний объем
            curr = {
                "standart": True,
                "volume_col": stand.col_water, 
                "volume_hot": stand.col_water,
                "volume_sewage": (stand.col_water + stand.col_water) * sq_appa,
                "period": (period - datetime.timedelta(days=1))
                }

        subs = Subsidies.get_items(user.id)
        priv = Privileges.get_items(user.id)
        recl = Recalculations.get_last_val(user.id)

        for el in rate:
            calc = get_calc_service(el, curr, sq_appa, subs, priv, recl)
            data.append(calc)
            total += calc["total"]
            pre_total += calc["pre_total"]
      
        update_values = {
            "data": json.dumps(data, ensure_ascii=False, default=str),
            "total": decimal.Decimal(total),
            "pre_total": decimal.Decimal(pre_total)
        }
        obj, created = VariablePayments.objects.update_or_create(
            user=user_id, period=period, defaults=update_values
        )
    return (data, total, pre_total)

# Делает расчет всех полей по Услуге
def get_calc_service(el, curr, sq_appa, subs, priv, recl):
    element = dict()
    water = False
    element["service"] = el.name
    element["unit"] = el.unit
    element["standart"] = 0
    element["rate"] = el.rate
    if re.search(r'холодная', el.name.lower()):
        element["volume"] = curr["volume_col"]
        water = True
    elif re.search(r'горячая', el.name.lower()):
        element["volume"] = curr["volume_hot"]
        water = True
    if not curr["standart"] and water:
        element["accured"] = el.rate * element["volume"]
    elif curr["standart"] and water:
        element["accured"] = el.rate * element["volume"] * sq_appa
    if re.search(r'водоотведение', el.name.lower()):
        element["volume"] = curr["volume_sewage"]
        element["accured"] = el.rate * curr["volume_sewage"]
    #TODO Электирчество кончилось... Кина не будет
    # if el.name == "Электроэнергия (день)" and prof.type_electric_meter == 2:
    #     accured = el.rate * (curr.electric_day - hist.hist_electric_day)
    # elif el.name == "Электроэнергия (ночь)" and prof.type_electric_meter == 2:
    #     accured = el.rate * (curr.electric_night - hist.hist_electric_night)
    # elif el.name == "Электроэнергия" and prof.type_electric_meter == 1:
    #     accured = el.rate * curr.electric_single
    element["coefficient"] = el.factor if el.factor > 0 else 1
    element["pre_total"] = (element["accured"] * element["coefficient"])
    element["subsidies"] = element["pre_total"] * decimal.Decimal(get_sale(el.name, subs)/ 100)
    element["privileges"] = element["pre_total"] * decimal.Decimal(get_sale(el.name, priv)/ 100)
    element["recalculation"] = get_recl(el.name, recl)
    element["total"] = (element["accured"] * element["coefficient"]) - (element["subsidies"] + element["privileges"]) + element["recalculation"]
    return (element)

# Готовит данные для шапки (персональные, реквизиты)
#TODO повесить сигналы на модели чтоб данные при изменении обновлялись
def get_head_data():
    users = User.objects.filter(is_staff=False)

    for user in users:
        data = dict()
        appa = Appartament.get_item(user.id)[0]
        uk = UK.get_item(appa.house.uk_id)

        data["payer"] = user.name # Плательщик
        data["address"] = appa
        data["sq_appart"] = appa.sq_appart # Площадь квартиры
        data["num_living"] = appa.num_owner # Кол-во проживающих
        data["name_uk"] = UK.get_full_name(uk.id) # Название, адрес, тел. и т.д. УК
        data["requisites"] = UK.get_requisites(uk.id) # Название, адрес, тел. и т.д. УК
        data["personal_account"] = user.personal_account # Номер лицевого счета

        update_values = {
            "data": json.dumps(data, ensure_ascii=False, default=str),
        }
        obj, created = HeaderData.objects.update_or_create(
            user=user, defaults=update_values
        )

# Возваращает субсидию или льготу при наличии или 0
def get_sale(name, arr):
    for el in arr:
        if el.service.name == name:
            return el.sale
        else:
            return 0
    return 0

# Возваращает перерасчет при наличии или 0
def get_recl(name, arr):
    for el in arr:
        if el.service.name == name:
            return el.recalc
        else:
            return 0
    return 0 
