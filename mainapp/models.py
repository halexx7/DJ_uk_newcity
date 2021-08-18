import datetime
from decimal import Decimal

from django.contrib.postgres.fields import JSONField
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now
from django.core.validators import MinValueValidator

from authnapp.models import User
from directory.models import House, Services

# PERIOD = datetime.datetime.now().date().replace(day=1, month=10)

# Общедомовой счетчик (ТЕКУЩИЕ показания)
class HouseCurrent(models.Model):
    period = models.DateField(verbose_name="Создан", default=datetime.datetime.now().replace(day=1))
    house = models.ForeignKey(House, verbose_name="Дом", null=True, on_delete=SET_NULL)
    col_water = models.DecimalField(verbose_name="Хол.вода", null=True, default=None, max_digits=8, decimal_places=3, validators=[MinValueValidator(0.001)])
    hot_water = models.DecimalField(verbose_name="Гор.вода", null=True, default=None, max_digits=8, decimal_places=3, validators=[MinValueValidator(0.001)])
    # electric_day = models.PositiveIntegerField(verbose_name="Электр.день", null=True, default=None)
    # electric_night = models.PositiveIntegerField(verbose_name="Электр.ночь", null=True, default=None)

    created = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Обновлен", auto_now=True)

    class Meta:
        ordering = ("-updated",)
        verbose_name = "Домовой счетчик (текущий)"
        verbose_name_plural = "Домовые счетчики (текущие)"
        # unique_together = ('house',)
    
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

    def delete(self):
        self.is_active = False
        self.save()


# Общедомовой счетчик (ИСТОРИЯ показания)
class HouseHistory(models.Model):
    period = models.DateField(verbose_name="Создан", default=datetime.datetime.now().replace(day=1))
    house = models.ForeignKey(House, verbose_name="Дом", null=True, on_delete=SET_NULL)
    col_water = models.DecimalField(verbose_name="Хол.вода", null=True, max_digits=8, decimal_places=3, validators=[MinValueValidator(0.001)])
    hot_water = models.DecimalField(verbose_name="Гор.вода", null=True, max_digits=8, decimal_places=3, validators=[MinValueValidator(0.001)])
    # electric_day = models.PositiveIntegerField(verbose_name="Электр.день", null=True, default=None)
    # electric_day = models.PositiveIntegerField(verbose_name="Электр.день", null=True)
    # electric_night = models.PositiveIntegerField(verbose_name="Электр.ночь", null=True)

    created = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Обновлен", auto_now=True)

    class Meta:
        ordering = ("-updated",)
        verbose_name = "Домовой счетчик (история)"
        verbose_name_plural = "Домовые счетчики (история)"
        # unique_together = ('period', 'house',)

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

    def delete(self):
        self.is_active = False
        self.save()

    # При удалении ловим и сохраняем объект ДОМОВЫЕ ПОКАЗАНИЯ
    @receiver(pre_delete, sender=HouseCurrent)
    def copy_arhive_current_to_history_house(sender, instance, **kwargs):
        house = instance.house_id
        period = instance.period
        print(type(instance.col_water))
        upd_val = {
            "col_water": instance.col_water,
            "hot_water": instance.hot_water,
            # "electric_day": instance.electric_day,
            # "electric_night": instance.electric_night,
        }
        obj, created = HouseHistory.objects.update_or_create(house_id=house, period=period, defaults=upd_val)


# Среднедомовой показатель
class Standart(models.Model):
    period = models.DateField(verbose_name="Создан", default=datetime.datetime.now().replace(day=1))
    house = models.ForeignKey(House, verbose_name="Дом", null=True, on_delete=SET_NULL)
    # Значения хранятся на 1 кв.м
    col_water = models.DecimalField(verbose_name="Норматив ХВС", max_digits=11, decimal_places=6)
    hot_water = models.DecimalField(verbose_name="Норматив ХГС", max_digits=11, decimal_places=6)
    # electric_day = models.DecimalField(
    #     verbose_name="Норматив ЭЛ.День", max_digits=6, decimal_places=2, null=True, default=None
    # )
    # electric_night = models.DecimalField(
    #     verbose_name="Нориматив ЭЛ.Ночь", max_digits=6, decimal_places=2, null=True, default=None
    # )

    created = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Обновлен", auto_now=True)

    class Meta:
        ordering = ("-period",)
        verbose_name = "Норматив"
        verbose_name_plural = "Нормативы"

    def __str__(self):
        return f"Период {self.period} - ул.{self.house.street.street}, д.{self.house.number}"

    @staticmethod
    def get_last_val(house):
        return Standart.objects.filter(house=house).first()

    def delete(self):
        self.is_active = False
        self.save()

    # При изменении текущих домовых показаний перещитываем норматив
    @receiver(post_save, sender=HouseCurrent)
    def calculation_of_standart_to_house_current(sender, instance, **kwargs):
        house = instance.house_id
        period = instance.period
        hist = HouseHistory.get_last_val(house)[0]
        sq = House.get_item(house)[0].sq_home
        upd_val = {
            "col_water": (Decimal(instance.col_water) - Decimal(hist.col_water)) / sq,
            "hot_water": (Decimal(instance.hot_water) - Decimal(hist.hot_water)) / sq,
            # "electric_day": instance.electric_day,
            # "electric_night": instance.electric_night,
        }
        obj, created = Standart.objects.update_or_create(house_id=house, period=period, defaults=upd_val)


# Текущие показания счетчиков (индивидуальные)
class CurrentCounter(models.Model):
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=CASCADE)
    period = models.DateField(verbose_name="Создан", default=datetime.datetime.now().replace(day=1))
    col_water = models.DecimalField(verbose_name="Хол.вода", null=True, max_digits=8, decimal_places=3, validators=[MinValueValidator(0.001)])
    hot_water = models.DecimalField(verbose_name="Гор.вода", null=True, max_digits=8, decimal_places=3, validators=[MinValueValidator(0.001)])
    # electric_day = models.PositiveIntegerField(verbose_name="Электроэнергия день", null=True, blank=True, default=None)
    # electric_night = models.PositiveIntegerField(
    #     verbose_name="Электроэнергия ночь", null=True, blank=True, default=None
    # )
    # electric_single = models.PositiveIntegerField(verbose_name="Электроэнергия", null=True, blank=True, default=None)

    created = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Обновлен", auto_now=True)

    class Meta:
        ordering = ("-period",)
        verbose_name = "Индивид. счетчик (текущий)"
        verbose_name_plural = "Индивид. счетчики (текущие)"

    def __str__(self):
        return f"({self.user.personal_accaunt}) - {self.user.name} ({self.period})"

    @staticmethod
    def get_last_val(user):
        period=datetime.datetime.now().replace(day=1, month=11)
        try:
            obj=CurrentCounter.objects.filter(user=user).latest("period")
            if obj.period.month == period.month:
                return obj
            else:
                return None
        except:
            return None


# История показания счетчиков (индивидуальные)
class HistoryCounter(models.Model):
    user = models.ForeignKey(User, verbose_name="Пользователь", null=True, on_delete=SET_NULL)
    period = models.DateField(verbose_name="Создан", default=datetime.datetime.now().replace(day=1))
    col_water = models.DecimalField(verbose_name="Хол.вода", null=True, max_digits=8, decimal_places=3, validators=[MinValueValidator(0.001)])
    hot_water = models.DecimalField(verbose_name="Гор.вода", null=True, max_digits=8, decimal_places=3, validators=[MinValueValidator(0.001)])
    # electric_day = models.PositiveIntegerField(verbose_name="Электр.день", null=True, blank=True)
    # electric_night = models.PositiveIntegerField(verbose_name="Электр.ночь", null=True, blank=True)
    # electric_single = models.PositiveIntegerField(verbose_name="Электр.однотариф", null=True, blank=True)

    created = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Обновлен", auto_now=True)

    class Meta:
        ordering = ("-period",)
        verbose_name = "Индивид. счетчик (история)"
        verbose_name_plural = "Индивид. счетчики (история)"

    def __str__(self):
        return f"({self.user.personal_account}) - {self.user.name} ({self.period})"

    @staticmethod
    def get_last_val(user):
        return HistoryCounter.objects.filter(user=user).first()

    def delete(self):
        self.is_active = False
        self.save()

    # При удалении ловим и сохраняем объект ИНДИВИДУАЛЬНЫЕ ПОКАЗАНИЯ
    @receiver(pre_delete, sender=CurrentCounter)
    def copy_arhive_current_to_history(sender, instance, **kwargs):
        user = instance.user
        period = instance.period
        upd_val = {
            "col_water": instance.col_water,
            "hot_water": instance.hot_water,
            # "electric_day": instance.electric_day,
            # "electric_night": instance.electric_night,
        }
        obj, created = HistoryCounter.objects.update_or_create(user=user, period=period, defaults=upd_val)


# Перерасчеты
class Recalculations(models.Model):
    user = models.ForeignKey(User, verbose_name="Пользователь", null=True, on_delete=SET_NULL)
    period = models.DateField(verbose_name="Создан", default=datetime.datetime.now().replace(day=1))
    service = models.ForeignKey(Services, verbose_name="Услуга", null=True, on_delete=SET_NULL)
    recalc = models.DecimalField(verbose_name="Сумма", max_digits=10, decimal_places=2, default=0)
    desc = models.TextField(verbose_name="Описание", blank=True, null=True)

    created = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Обновлен", auto_now=True)

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

    def delete(self):
        self.is_active = False
        self.save()


# Постоянные платежи (расчет по формуле = const*rate или = const)
class ConstantPayments(models.Model):
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=CASCADE)
    data = JSONField(verbose_name="data")
    total = models.DecimalField(verbose_name="Сумма", max_digits=8, decimal_places=3)
    pre_total = models.DecimalField(verbose_name="Сумма", max_digits=8, decimal_places=3)

    created = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Обновлен", auto_now=True)

    class Meta:
        verbose_name = "Платеж (постоянные)"
        verbose_name_plural = "Платежи (постоянные)"

    def __str__(self):
        return f"({self.user.personal_accaunt}) - {self.user.name}"

    @staticmethod
    def get_item(user):
        return ConstantPayments.objects.filter(user=user)

    def delete(self):
        self.is_active = False
        self.save()


# Переменные платежи (зависящие от счетчиков)
class VariablePayments(models.Model):
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=CASCADE)
    period = models.DateField(verbose_name="Создан", default=datetime.datetime.now().replace(day=1))
    data = JSONField(verbose_name="data")
    total = models.DecimalField(verbose_name="Итого", max_digits=10, decimal_places=2, default=0)
    pre_total = models.DecimalField(verbose_name="Итого", max_digits=10, decimal_places=2, default=0)

    created = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Обновлен", auto_now=True)

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

    def delete(self):
        self.is_active = False
        self.save()


# Данные для шапки платежки
class HeaderData(models.Model):
    user = models.ForeignKey(User, verbose_name="Пользователь", null=True, on_delete=SET_NULL)
    data = JSONField(verbose_name="Данные")

    created = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Обновлен", auto_now=True)

    class Meta:
        verbose_name = "Начисление"
        verbose_name_plural = "Начисления"

    def __str__(self):
        return f"({self.user.personal_accaunt}) - {self.user.name}"

    @staticmethod
    def get_item(user):
        return HeaderData.objects.filter(user=user).first()

    def delete(self):
        self.is_active = False
        self.save()


# Главная книга (дебет / кредит)
class MainBook(models.Model):
    DEBIT = "D"
    CREDIT = "C"

    DIRECTION_TRAVEL = ((DEBIT, "Оплата"), (CREDIT, "Начисление"))

    user = models.ForeignKey(User, verbose_name="Пользователь", null=True, on_delete=SET_NULL)
    period = models.DateField(verbose_name="Создан", default=datetime.datetime.now().replace(day=1))
    direction = models.CharField(verbose_name="Направление", max_length=1, choices=DIRECTION_TRAVEL)
    amount = models.DecimalField(verbose_name="Сумма", max_digits=12, decimal_places=2)

    created = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Обновлен", auto_now=True)

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
        """ Возвращает оплаты за указанный месяц """
        debit = MainBook.objects.filter(user=user, period=period, direction="D")
        return sum(abs(d.amount) for d in debit)

    @staticmethod
    def get_qty_last_items(qty):
        return MainBook.objects.filter(direction="D").order_by(
            "-updated",
        )[:qty]

    def delete(self):
        self.is_active = False
        self.save()

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
class PaymentOrder(models.Model):
    user = models.ForeignKey(User, verbose_name="Пользователь", null=True, on_delete=SET_NULL)
    period = models.DateField(verbose_name="Создан", default=datetime.datetime.now().replace(day=1))
    header_data = JSONField(verbose_name="Данные для шапки", null=True, default=None)
    constant_data = JSONField(verbose_name="Постоянная часть")
    variable_data = JSONField(verbose_name="Переменная часть")
    # Чистая сумма - за вычетом субсидий, льгот, перерасчетов и т.д.
    amount = models.DecimalField(verbose_name="Чистая_сумма", max_digits=7, decimal_places=2)
    # Грязная сумма - до вычетов
    pre_amount = models.DecimalField(verbose_name="Грязная сумма", max_digits=7, decimal_places=2)

    created = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Обновлен", auto_now=True)

    class Meta:
        ordering = ("-period",)
        verbose_name = "Начисление"
        verbose_name_plural = "Начисления"

    def __str__(self):
        return f"({self.user.personal_accaunt}) - {self.user.name} ({self.period})"

    def get_last_val(self):
        return PaymentOrder.objects.filter(user=self.user)[0:1]

    @staticmethod
    def get_item(order_id):
        return PaymentOrder.objects.filter(id=order_id)

    def delete(self):
        self.is_active = False
        self.save()

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
        #TODO PERIOD
        from invoice.views import PERIOD
        period = PERIOD
        header_data = HeaderData.objects.get(user=user)
        PaymentOrder.objects.filter(user=user, period=period).update(header_data=header_data.data)


# Текущее состояние счета
class PersonalAccountStatus(models.Model):
    user = models.OneToOneField(User, verbose_name="Пользователь", on_delete=CASCADE)
    amount = models.DecimalField(verbose_name="Состояние", max_digits=8, decimal_places=2)

    created = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Обновлен", auto_now=True)

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

    def delete(self):
        self.is_active = False
        self.save()

    @receiver(post_save, sender=MainBook)
    def get_update_data(sender, instance, **kwargs):
        user = instance.user
        debit = sender.get_user_debit(user=user)
        credit = sender.get_user_credit(user=user)
        debit_sum = sum(abs(d.amount) for d in debit)
        credit_sum = sum(abs(c.amount) for c in credit)
        upd_val = {
            "amount": (credit_sum - debit_sum),
        }
        obj, created = PersonalAccountStatus.objects.update_or_create(user=user, defaults=upd_val)

    @receiver(post_save, sender=Recalculations)
    def get_update_recalc(sender, instance, **kwargs):
        user = instance.user
        # period = datetime.datetime.now().replace(day=1)
        #TODO PERIOD
        from invoice.views import PERIOD
        period = PERIOD
        debit = sender.get_user_debit(user=user)
        credit = sender.get_user_credit(user=user)
        debit_sum = sum(abs(d.amount) for d in debit)
        credit_sum = sum(abs(c.amount) for c in credit)
        recalc = sender.get_sum_period(period)
        upd_val = {
            "amount": (credit_sum - debit_sum) + recalc,
        }
        obj, created = PersonalAccountStatus.objects.update_or_create(user=user, defaults=upd_val)


# Накопительный БУФФЕР средних начислений
class AverageСalculationBuffer(models.Model):
    """Накапливаем сумму начислений при расчете по общедомовым счетчикам"""
    user = models.OneToOneField(User, verbose_name="Пользователь", on_delete=CASCADE)
    col_water = models.DecimalField(verbose_name="Буффер холодной воды", max_digits=10, decimal_places=2, null=True, default=None)
    hot_water = models.DecimalField(verbose_name="Буффер горячей воды", max_digits=10, decimal_places=2, null=True, default=None)
    sewage = models.DecimalField(verbose_name="Буффер сточных вод", max_digits=10, decimal_places=2, null=True, default=None)

    created = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Обновлен", auto_now=True)

    class Meta:
        verbose_name = "Буффер средних начислений"

    def __str__(self):
        return f"({self.user.personal_accaunt}) - {self.user.name}"

    @staticmethod
    def get_item(user):
        try:
            buff = AverageСalculationBuffer.objects.filter(user=user).first()
            return buff
        except:
            return False

    def get_dict(self):
        data = dict()
        data["user"] = self.user
        data["col_water"] = self.col_water
        data["hot_water"] = self.hot_water
        data["sewage"] = self.sewage
        return data
            