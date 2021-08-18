import datetime
import decimal
import json
import re

from django.core.serializers import serialize
from django.utils.safestring import mark_safe
from django.views.generic.detail import DetailView

from authnapp.models import User
from personalacc.models import SiteConfiguration
from mainapp.models import (
    ConstantPayments,
    CurrentCounter,
    HeaderData,
    HistoryCounter,
    MainBook,
    PaymentOrder,
    PersonalAccountStatus,
    Recalculations,
    Standart,
    VariablePayments,
    AverageСalculationBuffer,
)
from directory.models import (
    Appartament,
    Privileges,
    Services,
    Subsidies,
)

PERIOD = datetime.datetime.now().date().replace(day=1, month=11)

def main(request):
    pass

class InvoiceViews(DetailView):
    model = PaymentOrder
    template_name = "invoice/invoice.html"

    def get_context_data(self, **kwargs):
        pk = self.kwargs["pk"]
        user = self.request.user
        pay_order = PaymentOrder.get_item(pk)
        context = super().get_context_data(**kwargs)
        context["order"] = mark_safe(serialize("json", pay_order))
        context["status"] = mark_safe(serialize("json", PersonalAccountStatus.get_item(user)))
        context["paid"] = MainBook.get_user_period_item(user, pay_order[0].period)
        return context

def starter():
    """Расчитываем все платежки"""
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
            "pre_total": decimal.Decimal(total),
        }
        obj, created = ConstantPayments.objects.update_or_create(user=user_id, defaults=update_values)
    return (data, total)

# Расчет ПЕРЕМЕННЫХ платежей (по сигналу)
# TODO Пока реализовано нажитием кнопки расчитать у менеджера!
def get_calc_variable():
    users = User.objects.filter(is_staff=False)
    rate = Services.get_varybose_payments(1)

    for user in users:
        data = []
        total = 0
        pre_total = 0
        # period = datetime.datetime.now().replace(day=1)
        #TODO PERIOD
        period = PERIOD
        user = User.objects.get(id=user.id)
        appa = Appartament.get_item(user.id)[0]
        stand = Standart.get_last_val(appa.house_id)
        sq_appa = appa.sq_appart
        hist = HistoryCounter.get_last_val(user.id)
        curr = {
            "user": user,
            "standart": False,
        }

        object_curr = CurrentCounter.get_last_val(user)
        if object_curr:
            # Если счетчики введены, считаем объем
            curr["period"] = object_curr.period
            curr["volume_col"] = (object_curr.col_water - hist.col_water)
            curr["volume_hot"] = (object_curr.hot_water - hist.hot_water)
            curr["volume_sewage"] = curr["volume_col"] + curr["volume_hot"]
            # Проверяем наличие данных в буфере накопительных платежей для перерасчета
            curr["buffer"] = AverageСalculationBuffer.get_item(user)
        else:
            # Если счетчики не введены, берем общедомовой средний объем
            curr["standart"] = True
            curr["volume_col"] = stand.col_water * sq_appa
            curr["volume_hot"] = stand.hot_water * sq_appa
            curr["volume_sewage"] = curr["volume_col"] + curr["volume_hot"]
            curr["period"] = period - datetime.timedelta(days=1)

        subs = Subsidies.get_items(user.id)
        priv = Privileges.get_items(user.id)
        recl = Recalculations.get_items(user)

        for el in rate:
            calc = get_calc_service(el, curr, sq_appa, subs, priv, recl)
            data.append(calc)
            total += calc["total"]
            pre_total += calc["pre_total"]

        update_values = {
            "data": json.dumps(data, ensure_ascii=False, default=str),
            "total": decimal.Decimal(total),
            "pre_total": decimal.Decimal(pre_total),
        }
        obj, created = VariablePayments.objects.update_or_create(user=user, period=period, defaults=update_values)
    return (data, total, pre_total)

# Готовит данные для шапки (персональные, реквизиты)
# TODO повесить сигналы на модели чтоб данные при изменении обновлялись
def get_head_data():
    users = User.objects.filter(is_staff=False)

    for user in users:
        data = dict()
        appa = Appartament.get_item(user.id)[0]
        uk = SiteConfiguration.get_solo()

        data["payer"] = user.name  # Плательщик
        data["address"] = appa
        data["sq_appart"] = appa.sq_appart  # Площадь квартиры
        data["num_living"] = appa.num_owner  # Кол-во проживающих
        data["name_uk"] = uk.get_full_name()  # Название, адрес, тел. и т.д. УК
        data["requisites"] = uk.get_requisites()  # Название, адрес, тел. и т.д. УК
        data["personal_account"] = user.personal_account  # Номер лицевого счета

        update_values = {
            "data": json.dumps(data, ensure_ascii=False, default=str),
        }
        obj, created = HeaderData.objects.update_or_create(user=user, defaults=update_values)


# Делает расчет всех полей по Услуге
def get_calc_service(el, curr, sq_appa, subs, priv, recl):
    element = dict()
    water = False
    #TODO PERIOD
    period = PERIOD
    element["service"] = el.name
    element["unit"] = el.unit
    element["standart"] = 0
    element["rate"] = el.rate

    if re.search(r"холодная", el.name.lower()):
        element["volume"] = curr["volume_col"]
        service = "col_water"
    elif re.search(r"горячая", el.name.lower()):
        element["volume"] = curr["volume_hot"]
        service = "hot_water"
    elif re.search(r"водоотведение", el.name.lower()):
        element["volume"] = curr["volume_sewage"]
        service = "sewage"

    if not curr["standart"]:
        element["accured"] = el.rate * element["volume"]
        if curr["buffer"]:
            #TODO PERIOD
            # period = datetime.datetime.now().replace(day=1)
            buffer = curr["buffer"].get_dict()
            upd_val = {
                "user": curr["user"],
                #TODO В какую сторону перерасчет???
                "recalc": element["accured"] - buffer[service],
                "desc": f"Автоматический перерасчет на основании введенных пользователем счетчиков"
            }
            obj, created = Recalculations.objects.update_or_create(user=curr['user'], period=period, service=el, defaults=upd_val)
            if service == "col_water":
                AverageСalculationBuffer.objects.filter(user=curr["user"]).update(col_water=0)
            elif service == "hot_water":
                AverageСalculationBuffer.objects.filter(user=curr["user"]).update(hot_water=0)
            elif service == "sewage":
                AverageСalculationBuffer.objects.filter(user=curr["user"]).update(sewage=0)

    elif curr["standart"]:
        element["accured"] = el.rate * decimal.Decimal(element["volume"])
        obj = AverageСalculationBuffer.get_item(curr['user'])
        if not obj:
            AverageСalculationBuffer.objects.create(user=curr['user'])
            obj = AverageСalculationBuffer.get_item(curr['user'])
        upd_bufer(obj, el.name, element["accured"])

    # TODO Электирчество кончилось... Кина не будет
    # if el.name == "Электроэнергия (день)" and prof.type_electric_meter == 2:
    #     accured = el.rate * (curr.electric_day - hist.hist_electric_day)
    # elif el.name == "Электроэнергия (ночь)" and prof.type_electric_meter == 2:
    #     accured = el.rate * (curr.electric_night - hist.hist_electric_night)
    # elif el.name == "Электроэнергия" and prof.type_electric_meter == 1:
    #     accured = el.rate * curr.electric_single
    element["coefficient"] = el.factor if el.factor > 0 else 1
    element["pre_total"] = element["accured"] * element["coefficient"]
    element["subsidies"] = element["pre_total"] * decimal.Decimal(get_sale(el.name, subs) / 100)
    element["privileges"] = element["pre_total"] * decimal.Decimal(get_sale(el.name, priv) / 100)
    element["recalculation"] = get_recl(el.name, recl)
    element["total"] = (
        (element["accured"] * element["coefficient"])
        - (element["subsidies"] + element["privileges"])
        + element["recalculation"]
    )
    return element

# Возваращает субсидию или льготу при наличии или 0
def get_sale(name, arr):
    for el in arr:
        if el.service.name == name:
            return el.sale
        else:
            continue
    return 0

# Возваращает перерасчет при наличии или 0
def get_recl(name, arr):
    for el in arr:
        if el.service.name == name:
            return el.recalc
        else:
            continue
    return 0

#Обновляет буффер
def upd_bufer(obj, name_srv,  accured):
    if re.search(r"холодная", name_srv.lower()):
        new_volume = obj.col_water + accured if obj.col_water else accured
        volume_rec = new_volume.quantize(decimal.Decimal("1.00"))
        AverageСalculationBuffer.objects.filter(user=obj.user).update(col_water=volume_rec)
    elif re.search(r"горячая", name_srv.lower()):
        new_volume = obj.hot_water + accured if obj.hot_water else accured
        volume_rec = new_volume.quantize(decimal.Decimal("1.00"))
        AverageСalculationBuffer.objects.filter(user=obj.user).update(hot_water=volume_rec)
    elif re.search(r"водоотведение", name_srv.lower()):
        new_volume = obj.sewage + accured if obj.sewage else accured
        volume_rec = new_volume.quantize(decimal.Decimal("1.00"))
        AverageСalculationBuffer.objects.filter(user=obj.user).update(sewage=volume_rec)
