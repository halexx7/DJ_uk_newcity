import datetime
from decimal import Decimal

from django.contrib.postgres.fields import JSONField
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _

from authnapp.models import User
from directory.models import House, Services
from mainapp.mixins.utils import ActiveMixin, CreateUpdateMixin, WaterCounterMixin, PERIOD


# Общедомовой счетчик (ТЕКУЩИЕ показания)
class HouseCurrent(WaterCounterMixin):
    period = models.DateField(verbose_name="Период", default=datetime.datetime.now().replace(day=1))
    house = models.ForeignKey(House, verbose_name="Дом", null=True, on_delete=SET_NULL)

    class Meta:
        ordering = ("-updated",)
        verbose_name = "Домовой счетчик (текущий)"
        verbose_name_plural = "Домовые счетчики (текущие)"

    def clean(self):
        if self.col_water < 0.01 or self.hot_water < 0.01:
            raise ValidationError("Допустимы только положительные числа!")

    def __str__(self):
        return f"Период - {self.period}, ул.{self.house.street.street}, Дом №{self.house.number}, к.{self.house.add_number}"

    @staticmethod
    def get_item(user):
        return HouseCurrent.objects.filter(user=user)

    @staticmethod
    def get_qty_last_items(qty):
        return HouseCurrent.objects.all()[:qty]


# Общедомовой счетчик (ИСТОРИЯ показания)
class HouseHistory(WaterCounterMixin):
    period = models.DateField(verbose_name="Период", default=datetime.datetime.now().replace(day=1))
    house = models.ForeignKey(House, verbose_name="Дом", null=True, on_delete=SET_NULL)

    class Meta:
        ordering = ("-updated",)
        verbose_name = "Домовой счетчик (история)"
        verbose_name_plural = "01 Домовые счетчики (история)"

    def __str__(self):
        return f"Период - {self.period}, ул.{self.house.street.street}, Дом №{self.house.number}, к.{self.house.add_number}"

    @staticmethod
    # Вместо User - Appartaments?
    def get_item(user):
        return HouseHistory.objects.filter(user=user)

    @staticmethod
    def get_last_val(house):
        return HouseHistory.objects.filter(house=house)[0:1]

    @staticmethod
    def get_qty_last_items(qty):
        return HouseCurrent.objects.all()[:qty]

    # При удалении ловим и сохраняем объект ДОМОВЫЕ ПОКАЗАНИЯ
    @receiver(pre_delete, sender=HouseCurrent)
    def copy_arhive_current_to_history_house(sender, instance, **kwargs):
        house = instance.house_id
        period = instance.period
        print(type(instance.col_water))
        upd_val = {
            "col_water": instance.col_water,
            "hot_water": instance.hot_water,
        }
        obj, created = HouseHistory.objects.update_or_create(house_id=house, period=period, defaults=upd_val)


# Среднедомовой показатель
class Standart(ActiveMixin):
    period = models.DateField(verbose_name="Период", default=datetime.datetime.now().replace(day=1))
    house = models.ForeignKey(House, verbose_name="Дом", null=True, on_delete=SET_NULL)
    # Значения хранятся на 1 кв.м
    col_water = models.DecimalField(verbose_name="Норматив ХВС", max_digits=11, decimal_places=6)
    hot_water = models.DecimalField(verbose_name="Норматив ХГС", max_digits=11, decimal_places=6)

    class Meta:
        ordering = ("-period",)
        verbose_name = "Норматив"
        verbose_name_plural = "Нормативы"

    def __str__(self):
        return f"Период {self.period} - ул.{self.house.street.street}, д.{self.house.number}"

    @staticmethod
    def get_last_val(house):
        return Standart.objects.filter(house=house).first()

    # При изменении текущих домовых показаний перещитываем норматив
    @receiver(post_save, sender=HouseCurrent)
    def calculation_of_standart_to_house_current(sender, instance, **kwargs):
        house = instance.house_id
        period = PERIOD
        # # TODO PERIOD
        # period = instance.period
        hist = HouseHistory.get_last_val(house)[0]
        sq = House.get_item(house)[0].sq_home
        upd_val = {
            "col_water": (Decimal(instance.col_water) - Decimal(hist.col_water)) / sq,
            "hot_water": (Decimal(instance.hot_water) - Decimal(hist.hot_water)) / sq,
        }
        obj, created = Standart.objects.update_or_create(house_id=house, period=period, defaults=upd_val)


# Текущие показания счетчиков (индивидуальные)
class CurrentCounter(WaterCounterMixin):
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=CASCADE)
    period = models.DateField(verbose_name="Период", default=datetime.datetime.now().replace(day=1))

    class Meta:
        ordering = ("-period",)
        verbose_name = "Индивидуальный счетчик (текущий)"
        verbose_name_plural = "Индивидуальные счетчики (текущие)"

    def __str__(self):
        return f"({self.user.personal_accaunt}) - {self.user.name} ({self.period})"

    @staticmethod
    def get_last_val(user):
        # period = datetime.datetime.now().replace(day=1, month=11)
        # TODO PERIOD
        period = PERIOD
        try:
            obj = CurrentCounter.objects.filter(user=user).latest("period")
            if obj.period.month == period.month:
                return obj
            else:
                return None
        except:
            return None


# История показания счетчиков (индивидуальные)
class HistoryCounter(WaterCounterMixin):
    user = models.ForeignKey(User, verbose_name="Пользователь", null=True, on_delete=SET_NULL)
    period = models.DateField(verbose_name="Период", default=datetime.datetime.now().replace(day=1))

    class Meta:
        ordering = ("-period",)
        verbose_name = "Индивидуальный счетчик (история)"
        verbose_name_plural = "02 Индивидуальные счетчики (история)"

    def __str__(self):
        return f"({self.user.personal_account}) - {self.user.name} ({self.period})"

    @staticmethod
    def get_last_val(user):
        return HistoryCounter.objects.filter(user=user).first()

    # При удалении ловим и сохраняем объект ИНДИВИДУАЛЬНЫЕ ПОКАЗАНИЯ
    @receiver(pre_delete, sender=CurrentCounter)
    def copy_arhive_current_to_history(sender, instance, **kwargs):
        user = instance.user
        period = instance.period
        upd_val = {
            "col_water": instance.col_water,
            "hot_water": instance.hot_water,
        }
        obj, created = HistoryCounter.objects.update_or_create(user=user, period=period, defaults=upd_val)


# Перерасчеты
class Recalculations(ActiveMixin):
    user = models.ForeignKey(User, verbose_name="Пользователь", null=True, on_delete=SET_NULL)
    period = models.DateField(verbose_name="Период", default=datetime.datetime.now().replace(day=1))
    service = models.ForeignKey(Services, verbose_name="Услуга", null=True, on_delete=SET_NULL)
    recalc = models.DecimalField(verbose_name="Сумма", max_digits=10, decimal_places=2, default=0)
    desc = models.TextField(verbose_name="Описание", blank=True, null=True)
    is_auto = models.BooleanField(verbose_name="Автоматический", default=False)

    class Meta:
        ordering = ("-updated",)
        verbose_name = "Перерасчет"
        verbose_name_plural = "Перерасчеты"

    def __str__(self):
        return f"({self.user.personal_accaunt}) - {self.service} ({self.period})"

    @staticmethod
    def get_last_val(user):
        return Recalculations.objects.filter(user=user).first()

    @staticmethod
    def get_items(user):
        return Recalculations.objects.filter(user=user)

    def get_sum_period(self, period):
        recalc = Recalculations.objects.filter(user=self.user, period=period)
        return sum(abs(el.recalc) for el in recalc)

    @staticmethod
    def get_qty_last_items(qty):
        return Recalculations.objects.all()[:qty]


# Постоянные платежи (расчет по формуле = const*rate или = const)
class ConstantPayments(ActiveMixin):
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=CASCADE)
    data = JSONField(verbose_name="data")
    total = models.DecimalField(verbose_name="Сумма", max_digits=8, decimal_places=3)
    pre_total = models.DecimalField(verbose_name="Сумма", max_digits=8, decimal_places=3)

    class Meta:
        verbose_name = "Платеж (постоянные)"
        verbose_name_plural = "Платежи (постоянные)"

    def __str__(self):
        return f"({self.user.personal_accaunt}) - {self.user.name}"

    @staticmethod
    def get_item(user):
        return ConstantPayments.objects.filter(user=user)


# Переменные платежи (зависящие от счетчиков)
class VariablePayments(ActiveMixin):
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=CASCADE)
    period = models.DateField(verbose_name="Период", default=datetime.datetime.now().replace(day=1))
    data = JSONField(verbose_name="data")
    total = models.DecimalField(verbose_name="Итого", max_digits=10, decimal_places=2, default=0)
    pre_total = models.DecimalField(verbose_name="Итого", max_digits=10, decimal_places=2, default=0)

    class Meta:
        ordering = ("-period",)
        verbose_name = "Платеж (перепенные)"
        verbose_name_plural = "Платежи (переменные)"

    def __str__(self):
        return f"({self.user.personal_accaunt}) - {self.user.name} ({self.period})"

    @staticmethod
    def get_items(user):
        return VariablePayments.objects.filter(user=user)

    @staticmethod
    def get_last_val(user):
        try:
            value = VariablePayments.objects.filter(user=user).first()
            return value
        except:
            return None


# Данные для шапки платежки
class HeaderData(CreateUpdateMixin):
    user = models.ForeignKey(User, verbose_name="Пользователь", null=True, on_delete=SET_NULL)
    data = JSONField(verbose_name="Данные")

    class Meta:
        verbose_name = "(Платежка) данные шапки"
        verbose_name_plural = "(Платежка) данные шапок"

    def __str__(self):
        return f"({self.user.personal_accaunt}) - {self.user.name}"

    @staticmethod
    def get_item(user):
        return HeaderData.objects.filter(user=user).first()


# Главная книга (дебет / кредит)
class MainBook(ActiveMixin):
    DEBIT = "D"
    CREDIT = "C"

    DIRECTION_TRAVEL = ((DEBIT, "Оплата"), (CREDIT, "Начисление"))

    user = models.ForeignKey(User, verbose_name="Пользователь", null=True, on_delete=SET_NULL)
    period = models.DateField(verbose_name="Период", default=datetime.datetime.now().replace(day=1))
    direction = models.CharField(verbose_name="Направление", max_length=1, choices=DIRECTION_TRAVEL)
    amount = models.DecimalField(verbose_name="Сумма", max_digits=12, decimal_places=2)

    class Meta:
        ordering = ("-period",)
        verbose_name = "Главная книга"
        verbose_name_plural = "Главная книга"

    def __str__(self):
        return f"({self.user.personal_accaunt}) - {self.user.name}, {self.direction} ({self.period})"

    @staticmethod
    def get_user_debit(user):
        """ Возвращает все ОПЛАТЫ конкретного жильца"""
        return MainBook.objects.filter(user=user).filter(direction="D")

    @staticmethod
    def get_user_credit(user):
        """ Возвращает все НАЧИСЛЕНИЯ конкретного жильца"""
        return MainBook.objects.filter(user=user).filter(direction="C")

    def get_all_debit():
        """ Возвращает все ОПЛАТЫ на счет ВСЕ"""
        return MainBook.objects.filter(direction="D")

    def get_all_credit():
        """ Возвращает все НАЧИСЛЕНИЯ co счета ВСЕ"""
        return MainBook.objects.filter(direction="C")

    def get_user_period_item(user, period):
        """ Возвращает оплаты за указанный месяц"""
        debit = MainBook.objects.filter(user=user, period=period, direction="D")
        return sum(abs(d.amount) for d in debit)

    @staticmethod
    def get_qty_last_items(qty):
        return MainBook.objects.filter(direction="D").order_by(
            "-updated",
        )[:qty]

    # При изменении константных или переменных расчетов, обновляем данные
    @receiver(post_save, sender=ConstantPayments)
    @receiver(post_save, sender=VariablePayments)
    def procc_accrual_mainbook(sender, instance, **kwargs):
        user = instance.user
        variable = VariablePayments.get_last_val(user=user)
        if variable:
            const_total = ConstantPayments.objects.get(user=user)
            period = variable.period
            varia_total = VariablePayments.objects.filter(period=period).get(user=user)
            upd_val = {"amount": (const_total.total + varia_total.total)}
            obj, created = MainBook.objects.update_or_create(user=user, period=period, direction="C", defaults=upd_val)


# Начисления (Плетежка)
class PaymentOrder(ActiveMixin):
    user = models.ForeignKey(User, verbose_name="Пользователь", null=True, on_delete=SET_NULL)
    period = models.DateField(verbose_name="Период", default=datetime.datetime.now().replace(day=1))
    header_data = JSONField(verbose_name="Данные для шапки", null=True, default=None)
    constant_data = JSONField(verbose_name="Постоянная часть")
    variable_data = JSONField(verbose_name="Переменная часть")
    # Чистая сумма - за вычетом субсидий, льгот, перерасчетов и т.д.
    amount = models.DecimalField(verbose_name="Чистая_сумма", max_digits=7, decimal_places=2)
    # Грязная сумма - до вычетов
    pre_amount = models.DecimalField(verbose_name="Грязная сумма", max_digits=7, decimal_places=2)

    class Meta:
        ordering = ("-period",)
        verbose_name = "Платежка)"
        verbose_name_plural = "(Платежка)"

    def __str__(self):
        return f"({self.user.personal_accaunt}) - {self.user.name} ({self.period})"

    def get_last_val(self):
        return PaymentOrder.objects.filter(user=self.user)[0:1]

    @staticmethod
    def get_item(order_id):
        return PaymentOrder.objects.filter(id=order_id)

    @receiver(post_save, sender=MainBook)
    def procc_update_data(sender, instance, **kwargs):
        if instance.direction == "C":
            user = instance.user
            period = instance.period
            constant = ConstantPayments.objects.get(user=user)
            variable = VariablePayments.objects.filter(period=period).get(user=user)
            upd_val = {
                "constant_data": constant.data,
                "variable_data": variable.data,
                "amount": (constant.total + variable.total),
                "pre_amount": (constant.pre_total + variable.pre_total),
            }
            obj, created = PaymentOrder.objects.update_or_create(user=user, period=period, defaults=upd_val)

    @receiver(post_save, sender=HeaderData)
    def procc_update_headerdata(sender, instance, **kwargs):
        user = instance.user
        # period = datetime.datetime.now().replace(day=1)
        # TODO PERIOD
        period = PERIOD
        header_data = HeaderData.objects.get(user=user)
        PaymentOrder.objects.filter(user=user, period=period).update(header_data=header_data.data)


# Текущее состояние счета
class PersonalAccountStatus(CreateUpdateMixin):
    user = models.OneToOneField(User, verbose_name="Пользователь", on_delete=CASCADE)
    amount = models.DecimalField(verbose_name="Состояние", max_digits=8, decimal_places=2)

    class Meta:
        ordering = ("amount",)
        verbose_name = "Состояние счета"
        verbose_name_plural = "Состояния счетов"

    def __str__(self):
        return f"({self.user.personal_accaunt}) - {self.user.name} ({self.amount})"

    # Перерасчет, когда вносится?
    @staticmethod
    def get_item(user):
        return PersonalAccountStatus.objects.filter(user=user)

    @receiver(post_save, sender=Recalculations)
    @receiver(post_save, sender=MainBook)
    def get_update_data(sender, instance, **kwargs):
        user = instance.user
        debit = MainBook.get_user_debit(user=user)
        credit = MainBook.get_user_credit(user=user)
        debit_sum = sum(abs(d.amount) for d in debit)
        credit_sum = sum(abs(c.amount) for c in credit)
        upd_val = {
            "amount": (credit_sum - debit_sum),
        }
        obj, created = PersonalAccountStatus.objects.update_or_create(user=user, defaults=upd_val)


# Накопительный БУФФЕР средних начислений
class AverageСalculationBuffer(CreateUpdateMixin):
    """Накапливаем сумму начислений при расчете по общедомовым счетчикам"""

    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=CASCADE)
    period = models.DateField(verbose_name="Период", default=datetime.datetime.now().replace(day=1))
    col_water = models.DecimalField(
        verbose_name="Буффер холодной воды", max_digits=10, decimal_places=3, null=True, default=None
    )
    hot_water = models.DecimalField(
        verbose_name="Буффер горячей воды", max_digits=10, decimal_places=3, null=True, default=None
    )
    sewage = models.DecimalField(
        verbose_name="Буффер сточных вод", max_digits=10, decimal_places=3, null=True, default=None
    )

    class Meta:
        verbose_name = "Буффер средних начислений"
        unique_together = ('user', 'period')

    def __str__(self):
        return f"({self.user.personal_accaunt}) - {self.user.name}"

    @staticmethod
    def get_item(user):
        try:
            buff = AverageСalculationBuffer.objects.filter(user=user).first()
            return buff
        except:
            return False

    def get_sum_average_buffer(user):
        """ Возвращает оплаты за указанный месяц """
        items = AverageСalculationBuffer.objects.filter(user=user)
        data = {
            "user": user,
            "col_water": sum(abs(el.col_water) for el in items),
            "hot_water": sum(abs(el.hot_water) for el in items),
            "sewage": sum(abs(el.sewage) for el in items)}
        return data

    def get_dict(self):
        data = dict()
        data["user"] = self.user
        data["col_water"] = self.col_water
        data["hot_water"] = self.hot_water
        data["sewage"] = self.sewage
        return data
