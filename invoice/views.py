import datetime
import decimal
import json
import re
from datetime import timezone
import calendar
from newcity.celery import app

from django.core.serializers import serialize
from django.utils.safestring import mark_safe
from django.views.generic.detail import DetailView

from authnapp.models import User
from directory.models import Appartament, Privileges, Services, Subsidies
from mainapp.mixins.utils import PERIOD
from mainapp.models import (AverageСalculationBuffer, ConstantPayments,
                            CurrentCounter, HeaderData, HistoryCounter,
                            MainBook, PaymentOrder, PersonalAccountStatus,
                            Recalculations, Standart, VariablePayments)
from personalacc.models import SiteConfiguration


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
            element = {
                "service": el.name,
                "unit": el.unit,
                "rate": el.rate,
                "standart": "",
                "volume": "",
                "coefficient": el.factor if el.factor >= 0 else "",
                "subsidies": 0,
                "privileges": 0,
                "recalculation": 0,
            }
            if el.unit.name == "м2":
                element["accured"] = el.rate * appart.sq_appart
            elif el.unit.name == "чел":
                element["accured"] = el.rate * appart.num_owner
            else:
                element["accured"] = el.rate
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
        total, pre_total = 0, 0
        period = PERIOD
        user = User.objects.get(id=user.id)
        appa = Appartament.get_item(user.id)[0]
        stand = Standart.get_last_val(appa.house_id)
        sq_appa = appa.sq_appart
        hist = HistoryCounter.get_last_val(user.id)
        curr = {"user": user, "standart": False}
        object_curr = CurrentCounter.get_last_val(user)
        if object_curr:
            # Если счетчики введены, считаем объем
            curr["period"] = object_curr.period
            curr["volume_col"] = object_curr.col_water - hist.col_water
            curr["volume_hot"] = object_curr.hot_water - hist.hot_water
            curr["volume_sewage"] = curr["volume_col"] + curr["volume_hot"]
            # Проверяем наличие данных в буфере накопительных платежей для перерасчета
            curr["buffer"] = AverageСalculationBuffer.get_sum_average_buffer(user)
        else:
            # Если счетчики не введены, берем общедомовой средний объем
            curr["standart"] = True
            curr["volume_col"] = stand.col_water * sq_appa
            curr["volume_hot"] = stand.hot_water * sq_appa
            curr["volume_sewage"] = curr["volume_col"] + curr["volume_hot"]
            curr["period"] = PERIOD - datetime.timedelta(days=1)

        subs = Subsidies.get_items(user.id)
        priv = Privileges.get_items(user.id)

        for el in rate:
            calc = get_calc_service(el, curr, subs, priv)
            data.append(calc)
            total += calc["total"]
            pre_total += calc["pre_total"]

        update_values = {
            "data": json.dumps(data, ensure_ascii=False, default=str),
            "total": decimal.Decimal(total),
            "pre_total": decimal.Decimal(pre_total),
        }
        obj, created = VariablePayments.objects.update_or_create(user=user, period=PERIOD, defaults=update_values)
    return (data, total, pre_total)


# Готовит данные для шапки (персональные, реквизиты)
# TODO повесить сигналы на модели чтоб данные при изменении обновлялись
def get_head_data():
    users = User.objects.filter(is_staff=False)
    for user in users:
        appa = Appartament.get_item(user.id)[0]
        uk = SiteConfiguration.get_solo()
        data = {
            "payer": user.name,
            "address": appa,
            "sq_appart": appa.sq_appart,
            "num_living": appa.num_owner,  # Кол-во проживающих
            "name_uk": uk.get_full_name(),
            "requisites": uk.get_requisites(),
            "personal_account": user.personal_account,
        }
        update_values = {
            "data": json.dumps(data, ensure_ascii=False, default=str),
        }
        obj, created = HeaderData.objects.update_or_create(user=user, defaults=update_values)


# Делает расчет всех полей по Услуге
def get_calc_service(el, curr, subs, priv):
    element = dict()
    const = False
    element["service"] = el.name
    element["unit"] = el.unit
    element["standart"] = 0
    element["rate"] = el.rate

    if re.search(r"холодная", el.name.lower()):
        element["volume"] = curr["volume_col"]
        const = "col_water"
    elif re.search(r"горячая", el.name.lower()):
        element["volume"] = curr["volume_hot"]
        const = "hot_water"
    elif re.search(r"водоотведение", el.name.lower()):
        element["volume"] = curr["volume_sewage"]
        const = "sewage"

    if not curr["standart"]:
        element["accured"] = el.rate * decimal.Decimal(element["volume"])
        if curr["buffer"]:
            buffer = AverageСalculationBuffer.get_sum_average_buffer(curr["user"])
            if buffer[const]:
                upd_val = {
                    "user": curr["user"],
                    # TODO В какую сторону перерасчет???
                    "recalc": element["accured"] - curr["buffer"][const],
                    "desc": f"Автоматический перерасчет на основании введенных пользователем счетчиков",
                }
                obj, created = Recalculations.objects.update_or_create(
                    user=curr["user"], period=PERIOD, service=el, is_auto=True, defaults=upd_val
                )
                if const == "col_water":
                    AverageСalculationBuffer.objects.filter(user=curr["user"]).update(col_water=0)
                elif const == "hot_water":
                    AverageСalculationBuffer.objects.filter(user=curr["user"]).update(hot_water=0)
                elif const == "sewage":
                    AverageСalculationBuffer.objects.filter(user=curr["user"]).update(sewage=0)

    elif curr["standart"]:
        element["accured"] = el.rate * decimal.Decimal(element["volume"])
        obj, create = AverageСalculationBuffer.objects.get_or_create(user=curr["user"], period=PERIOD)
        upd_bufer(obj, el.name, element["accured"])
    recl = Recalculations.get_items(curr["user"], PERIOD)
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
    # TODO Если несколько записей, т.е. авто и не авто, то возвращать нужно сумму.
    for el in arr:
        if el.service.name == name:
            return el.recalc
        else:
            continue
    return 0


# Обновляет буффер
def upd_bufer(obj, name_srv, accured):
    volume_rec = accured.quantize(decimal.Decimal("1.00"))
    if re.search(r"холодная", name_srv.lower()):
        AverageСalculationBuffer.objects.filter(user=obj.user, period=PERIOD).update(col_water=volume_rec)
    elif re.search(r"горячая", name_srv.lower()):
        AverageСalculationBuffer.objects.filter(user=obj.user, period=PERIOD).update(hot_water=volume_rec)
    elif re.search(r"водоотведение", name_srv.lower()):
        AverageСalculationBuffer.objects.filter(user=obj.user, period=PERIOD).update(sewage=volume_rec)


def get_last_date():
    """Возвращает последнюю дату месяца"""
    today = timezone.now()
    year = today.year
    month = today.month
    last_date = calendar.monthrange(year, month)[1]
    return str(last_date)
