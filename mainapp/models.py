import datetime

from django.contrib.postgres.fields import JSONField
from django.db import models
from django.db.models.deletion import CASCADE, PROTECT
from django.db.models.lookups import In
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import get_object_or_404
from django.utils import timezone

from authnapp.models import User


class ServicesCategory(models.Model):
    name = models.CharField(verbose_name="Название", max_length=32)

    is_active = models.BooleanField(verbose_name="Активная", db_index=True, default=True)
    created = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Обновлен", auto_now=True)

    class Meta:
        verbose_name = "Категория услуг"
        verbose_name_plural = "004 Категории услуг"

    def __str__(self):
        return self.name


class Metrics(models.Model):
    name = models.CharField(verbose_name="Единица измерения", max_length=32)

    is_active = models.BooleanField(verbose_name="Активная", db_index=True, default=True)
    created = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Обновлен", auto_now=True)

    class Meta:
        verbose_name = "Единица измерения"
        verbose_name_plural = "003 Единицы измерения"

    def __str__(self):
        return self.name


class Services(models.Model):
    category = models.ForeignKey(ServicesCategory, verbose_name="Категория", on_delete=models.CASCADE, default=1)
    name = models.CharField(verbose_name="Услуга", max_length=256)
    unit = models.ForeignKey(Metrics, verbose_name="Единицы", on_delete=models.CASCADE)
    rate = models.DecimalField(verbose_name="Тариф", max_digits=7, decimal_places=3, default=0)
    factor = models.DecimalField(verbose_name="Коэфициент", max_digits=3, decimal_places=2, default=1)
    const = models.BooleanField(verbose_name="Константа", db_index=True, default=True)

    is_active = models.BooleanField(verbose_name="Активная", db_index=True, default=True)
    created = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Обновлен", auto_now=True)

    class Meta:
        verbose_name = "Услугу"
        verbose_name_plural = "005 Услуги"

    def __str__(self):
        return f"{self.name} ({self.category.name})"

    @staticmethod
    def get_const_payments(category):
        """Возвращает константные статьи (которые зависят от тарифа)"""
        return Services.objects.filter(is_active=True, const=True, category=category)

    @staticmethod
    def get_varybose_payments(category):
        """Возвращает переменные статьи (которые зависят от подачи показаний)"""
        return Services.objects.filter(is_active=True, const=False, category=category)

    @staticmethod
    def get_items():
        return Services.objects.filter(is_active=True)


class City(models.Model):
    city = models.CharField(verbose_name="Город", max_length=128)

    is_active = models.BooleanField(verbose_name="Активный", db_index=True, default=True)
    created = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Обновлен", auto_now=True)

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "001 Города"

    def __str__(self):
        return self.city


class Street(models.Model):
    street = models.CharField(verbose_name="Улица", max_length=128)

    is_active = models.BooleanField(verbose_name="Активный", db_index=True, default=True)
    created = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Обновлен", auto_now=True)

    class Meta:
        verbose_name = "Улица"
        verbose_name_plural = "002 Улицы"

    def __str__(self):
        return f'ул.{self.street}'


class UK(models.Model):
    name = models.CharField(verbose_name="Название", max_length=128)
    city = models.ForeignKey(City, verbose_name="Город", on_delete=models.CASCADE)
    street = models.ForeignKey(Street, verbose_name="Улица", on_delete=models.CASCADE)
    num_building = models.CharField(verbose_name="Номер здания", max_length=3)
    phone = models.CharField(verbose_name="Телефон", max_length=20)
    email = models.CharField(verbose_name="e-mail", max_length=128)
    inn = models.CharField(verbose_name="ИНН", max_length=10)
    ps = models.CharField(verbose_name="Расчетный счет", max_length=20)
    bik = models.CharField(verbose_name="БИК", max_length=10)
    ks = models.CharField(verbose_name="Кор.счет", max_length=20)
    bank = models.CharField(verbose_name="Банк", max_length=128)
    web_addr = models.CharField(verbose_name="Сайт", max_length=128)

    is_active = models.BooleanField(verbose_name="Активный", db_index=True, default=True)
    created = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Обновлен", auto_now=True)

    class Meta:
        verbose_name = "Управляющая компания"
        verbose_name_plural = "006 Управляющие компании"

    def __str__(self):
        return self.name


class House(models.Model):
    number = models.CharField(verbose_name="Номер", max_length=3)
    add_number = models.CharField(verbose_name="Корпус", max_length=3, blank=True, default='-')
    city = models.ForeignKey(City, verbose_name="Город", on_delete=models.CASCADE)
    street = models.ForeignKey(Street, verbose_name="Улица", on_delete=models.CASCADE)
    sq_home = models.DecimalField(verbose_name="Площадь", max_digits=7, decimal_places=2)
    uk = models.ForeignKey(UK, verbose_name="Управляющая компания", on_delete=CASCADE)
    category_rate = models.ForeignKey(ServicesCategory, verbose_name="Категория", on_delete=CASCADE, default=1)

    is_active = models.BooleanField(verbose_name="Активный", db_index=True, default=True)
    created = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Обновлен", auto_now=True)

    class Meta:
        verbose_name = "Дом"
        verbose_name_plural = "007 Дома"

    def __str__(self):
        return f'Дом №{self.number}, к.{self.add_number}, ул.{self.street.street}'


# Общедомовой счетчик (ТЕКУЩИЕ показания)
class HouseCurrent(models.Model):
    period = models.DateField(verbose_name="Создан", auto_now_add=True)
    house = models.ForeignKey(House, verbose_name="Дом", on_delete=models.CASCADE)
    col_water = models.PositiveIntegerField(verbose_name="Хол.вода", null=True)
    hot_water = models.PositiveIntegerField(verbose_name="Гор.вода", null=True)
    electric_day = models.PositiveIntegerField(verbose_name="Электр.день", null=True)
    electric_night = models.PositiveIntegerField(verbose_name="Электр.ночь", null=True)

    created = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Обновлен", auto_now=True)

    class Meta:
        verbose_name = "Домовой счетчик (текущий)"
        verbose_name_plural = "Домовые счетчики (текущие)"

    def __str__(self):
        return f'Период - {self.period}, ул.{self.house.street.street}, Дом №{self.house.number}, к.{self.house.add_number}'

    @staticmethod
    # Вместо User - Appartaments?
    def get_item(user):
        return HouseCurrent.objects.filter(user=user)


# Общедомовой счетчик (ИСТОРИЯ показания)
class HouseHistory(models.Model):
    period = models.DateField(verbose_name="Создан", auto_now_add=True)
    house = models.ForeignKey(House, verbose_name="Дом", on_delete=models.CASCADE)
    col_water = models.PositiveIntegerField(verbose_name="Хол.вода", null=True)
    hot_water = models.PositiveIntegerField(verbose_name="Гор.вода", null=True)
    electric_day = models.PositiveIntegerField(verbose_name="Электр.день", null=True)
    electric_night = models.PositiveIntegerField(verbose_name="Электр.ночь", null=True)

    created = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Обновлен", auto_now=True)

    class Meta:
        verbose_name = "Домовой счетчик (история)"
        verbose_name_plural = "Домовые счетчики (история)"
    
    def __str__(self):
        return f'Период - {self.period}, ул.{self.house.street.street}, Дом №{self.house.number}, к.{self.house.add_number}'

    @staticmethod
    # Вместо User - Appartaments?
    def get_item(user):
        return HouseHistory.objects.filter(user=user)

    
class Standart(models.Model):
    period = models.DateField(verbose_name="Период", auto_now_add=True)
    house = models.ForeignKey(House, verbose_name="Дом", on_delete=models.CASCADE)
    col_water = models.PositiveIntegerField(verbose_name="Хол.вода", null=True)
    hot_water = models.PositiveIntegerField(verbose_name="Гор.вода", null=True)
    electric_day = models.PositiveIntegerField(verbose_name="Электр.день", null=True)
    electric_night = models.PositiveIntegerField(verbose_name="Электр.ночь", null=True)

    class Meta:
        ordering = ("-period",)
        verbose_name = "Норматив"
        verbose_name_plural = "Нормативы"
    
    def __str__(self):
        return f'Период {self.period} - ул.{self.house.street.street}, д.{self.number}'

    @staticmethod
    def get_last_val(user):
        return Standart.objects.filter(user=user)[0:1]


class Appartament(models.Model):
    house = models.ForeignKey(House, verbose_name="Дом", on_delete=CASCADE)
    number = models.PositiveIntegerField(verbose_name="Номер")
    add_number = models.CharField(verbose_name="Комната", max_length=2, null=True, blank=True, default='-')
    sq_appart = models.DecimalField(verbose_name="Площадь", max_digits=5, decimal_places=2)
    num_owner = models.PositiveIntegerField(verbose_name="Кол-во проживающих", default=0)

    is_active = models.BooleanField(verbose_name="Активный", db_index=True, default=True)
    created = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Обновлен", auto_now=True)

    class Meta:
        verbose_name = "Квартира"
        verbose_name_plural = "008 Квартиры"

    def __str__(self):
        return f'ул.{self.house.street.street}, д.{self.house.number}, кв.{self.number}, комн.{self.add_number}'


class UserProfile(models.Model):
    SINGLE = "1"
    TWO = "2"
    MULTI = "3"

    COUNTER_TYPE = ((SINGLE, "однотарифный"), (TWO, "двухтарифный"), (MULTI, "многотарифный"))

    user = models.OneToOneField(User, null=False, db_index=True, on_delete=models.CASCADE)
    appartament = models.ForeignKey(Appartament, verbose_name="Квартира", on_delete=CASCADE, null=True)
    type_electric_meter = models.CharField(verbose_name="Тип счетчика", max_length=1, choices=COUNTER_TYPE)

    is_active = models.BooleanField(verbose_name="Активный", db_index=True, default=True)
    created = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Обновлен", auto_now=True)

    class Meta:
        ordering = ("updated",)
        verbose_name = "Профиль"
        verbose_name_plural = "009 Профили"

    def __str__(self):
        return f'{self.user.name} ({self.appartament})'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.userprofile.save()


# Текущие показания счетчиков (индивидуальные)
class CurrentCounter(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=CASCADE)
    col_water = models.PositiveIntegerField(verbose_name="Хол.вода", null=True)
    hot_water = models.PositiveIntegerField(verbose_name="Гор.вода", null=True)
    electric_day = models.PositiveIntegerField(verbose_name="Электр.день", null=True)
    electric_night = models.PositiveIntegerField(verbose_name="Электр.ночь", null=True)
    electric_single = models.PositiveIntegerField(verbose_name="Электр.однотариф", null=True, blank=True, default="")

    created = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Обновлен", auto_now=True)

    class Meta:
        verbose_name = "Индивид. счетчик (текущий)"
        verbose_name_plural = "Индивид. счетчики (текущие)"


    def __str__(self):
        return f'ул.{self.street.street}, д.{self.number}, кв.{self.number}'


    @staticmethod
    def get_item(user):
        return CurrentCounter.objects.filter(user=user)


# История показания счетчиков (индивидуальные)
class HistoryCounter(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name="Пользователь", on_delete=CASCADE)
    period = models.DateField(verbose_name="Период")
    hist_col_water = models.PositiveIntegerField(verbose_name="Гор.вода")
    hist_hot_water = models.PositiveIntegerField(verbose_name="Хол.вода")
    hist_electric_day = models.PositiveIntegerField(verbose_name="Электр.день")
    hist_electric_night = models.PositiveIntegerField(verbose_name="Электр.ночь")
    electric_single = models.PositiveIntegerField(verbose_name="Электр.однотариф", null=True, blank=True, default="")

    created = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Обновлен", auto_now=True)

    class Meta:
        ordering = ("-period",)
        verbose_name = "Индивид. счетчик (история)"
        verbose_name_plural = "Индивид. счетчики (история)"

    @staticmethod
    def get_last_val(user):
        return HistoryCounter.objects.filter(user=user)[0:1]


# Постоянные платежи (расчет по формуле = const*rate или = const)
class ConstantPayments(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name="Пользователь", on_delete=CASCADE)
    data = JSONField(verbose_name="data")

    created = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Обновлен", auto_now=True)

    @staticmethod
    def get_item(user):
        return ConstantPayments.objects.filter(user=user)

    class Meta:
        verbose_name = "Платеж (постоянные)"
        verbose_name_plural = "Платежи (постоянные)"


# Переменные платежи (зависящие от счетчиков)
class VariablePayments(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name="Пользователь", on_delete=CASCADE)
    period = models.DateField(verbose_name="Период")
    service = models.CharField(verbose_name="Услуга", max_length=128)
    unit = models.CharField(verbose_name="Ед.измерения", max_length=32)
    # TODO вынести в отдельную таблицу? (Уточнение у заказчика, как считается, исходя из счетчиков или константа)
    standart = models.DecimalField(verbose_name="Норматив", max_digits=8, decimal_places=4, blank=True, default="0")
    rate = models.DecimalField(verbose_name="Тариф", max_digits=7, decimal_places=3, default=0)
    accured = models.DecimalField(verbose_name="Начислено", max_digits=7, decimal_places=3, default=0)
    volume = models.DecimalField(verbose_name="Объем", max_digits=7, decimal_places=2, default=0)
    coefficient = models.DecimalField(verbose_name="Коэфициент", max_digits=3, decimal_places=2, default=1)
    subsidies = models.DecimalField(verbose_name="Субсидии", max_digits=6, decimal_places=2, default=0)
    privileges = models.DecimalField(verbose_name="Льготы", max_digits=6, decimal_places=2, default=0)
    recalculations = models.DecimalField(verbose_name="Перерасчет", max_digits=6, decimal_places=2, default=0)
    total = models.DecimalField(verbose_name="Итого", max_digits=7, decimal_places=2, default=0)

    created = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Обновлен", auto_now=True)

    class Meta:
        verbose_name = "Платеж (перепенные)"
        verbose_name_plural = "Платежи (переменные)"

    @staticmethod
    def get_items(user):
        return VariablePayments.objects.filter(user=user)


# Cубсидии
class Subsidies(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name="Пользователь", on_delete=PROTECT)
    service = models.ForeignKey(Services, verbose_name="Услуга", on_delete=PROTECT)
    sale = models.PositiveIntegerField(verbose_name="Субсидии", default=0)
    desc = models.TextField(verbose_name="Субсидии")

    is_active = models.BooleanField(verbose_name="Активный", db_index=True, default=True)
    created = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Обновлен", auto_now=True)
    desc = models.TextField(verbose_name="Описание", blank=True, null=True)

    class Meta:
        ordering = ("-updated",)
        verbose_name = "Субсидия"
        verbose_name_plural = "010 Субсидии"


    def __str__(self):
        return f'{self.user.user.name} ({self.user.user.personal_account}) - {self.service.name}'


    @staticmethod
    def get_items(user):
        return Subsidies.objects.filter(user=user)


# Льготы
class Privileges(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name="Пользователь", on_delete=PROTECT)
    service = models.ForeignKey(Services, verbose_name="Услуга", on_delete=PROTECT)
    sale = models.PositiveIntegerField(verbose_name="Льготы", default=0)

    is_active = models.BooleanField(verbose_name="Активный", db_index=True, default=True)
    created = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Обновлен", auto_now=True)
    desc = models.TextField(verbose_name="Описание", blank=True, null=True)

    class Meta:
        ordering = ("-updated",)
        verbose_name = "Льгота"
        verbose_name_plural = "011 Льготы"


    def __str__(self):
        return f'{self.user.user.name} ({self.user.user.personal_account}) - {self.service.name}'


    @staticmethod
    def get_items(user):
        return Subsidies.objects.filter(user=user)


# Начисления (Текущие)
class Profit(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name="Пользователь", on_delete=PROTECT)
    period = models.DateField(verbose_name="Период")
    amount_profit = models.DecimalField(verbose_name="Сумма", max_digits=7, decimal_places=2)
    variable = JSONField(verbose_name="variable")

    created = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Обновлен", auto_now=True)

    class Meta:
        ordering = ("-period",)
        verbose_name = "Начисление"
        verbose_name_plural = "Начисления"

    @staticmethod
    def get_last_val(user):
        return HistoryCounter.objects.filter(user=user)[0:1]


# Инфорамация по оплатам
class Payment(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name="Пользователь", on_delete=PROTECT)
    period = models.DateField(verbose_name="Период")
    amount_profit = models.DecimalField(verbose_name="Сумма", max_digits=7, decimal_places=2)

    created = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Обновлен", auto_now=True)

    class Meta:
        ordering = ("-period",)
        verbose_name = "Оплата"
        verbose_name_plural = "Оплаты"

    @staticmethod
    def get_last_val(user):
        return HistoryCounter.objects.filter(user=user)[0:1]


# Перерасчеты
class Recalculations(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name="Пользователь", on_delete=CASCADE)
    period = models.DateField(verbose_name="Период")
    recalc = models.DecimalField(verbose_name="Сумма", max_digits=7, decimal_places=2, default=0)
    desc = models.TextField(verbose_name="Описание", blank=True, null=True)

    created = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Обновлен", auto_now=True)

    class Meta:
        ordering = ("-period",)
        verbose_name = "Перерасчет"
        verbose_name_plural = "Перерасчеты"

    # Перерасчет, когда вносится?
    @staticmethod
    def get_last_val(user):
        return HistoryCounter.objects.filter(user=user)[0:1]
