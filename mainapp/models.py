import datetime

from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import JSONField
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.deletion import CASCADE, PROTECT, SET_NULL
from django.db.models.lookups import In
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

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
    
    def delete(self):
        self.is_active = False
        self.save()

    def delete(self):
        self.is_active = False
        self.save()


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

    def delete(self):
        self.is_active = False
        self.save()


class Services(models.Model):
    category = models.ForeignKey(
        ServicesCategory, verbose_name="Категория", related_name="category", on_delete=models.CASCADE, default=1
    )
    name = models.CharField(verbose_name="Услуга", max_length=256)
    unit = models.ForeignKey(Metrics, verbose_name="Единицы", related_name="unit", on_delete=models.CASCADE)
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
    
    def delete(self):
        self.is_active = False
        self.save()

    def delete(self):
        self.is_active = False
        self.save()


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
    
    def delete(self):
        self.is_active = False
        self.save()

    def delete(self):
        self.is_active = False
        self.save()


class Street(models.Model):
    city = models.ForeignKey(City, verbose_name="Город", on_delete=CASCADE)
    street = models.CharField(verbose_name="Улица", max_length=128)

    is_active = models.BooleanField(verbose_name="Активный", db_index=True, default=True)
    created = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Обновлен", auto_now=True)

    class Meta:
        verbose_name = "Улица"
        verbose_name_plural = "002 Улицы"

    def __str__(self):
        return f"ул.{self.street}"

    def delete(self):
        self.is_active = False
        self.save()


class UK(models.Model):
    name = models.CharField(verbose_name="Название", max_length=128)
    city = models.ForeignKey(City, verbose_name="Город", null=True, on_delete=SET_NULL)
    street = models.ForeignKey(Street, verbose_name="Улица", null=True, on_delete=SET_NULL)
    num_building = models.CharField(verbose_name="Номер здания", max_length=3)
    phone = models.CharField(
        verbose_name="Телефон", max_length=11, null=True, blank=True, help_text="Номер телефона в формате - 79823212334"
    )
    email = models.EmailField(verbose_name="e-mail")
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

    @staticmethod
    def get_item(uk):
        return House.objects.get(id=uk)

    @staticmethod
    def get_full_name(uk):
        uk = UK.objects.get(id=uk)
        name = {
            "name": uk.name,
            "address": f'{uk.street}, д.{uk.num_building}',
            "phone": f'тел.{uk.phone}',
            "web": uk.web_addr
        }
        return name

    @staticmethod
    def get_requisites(uk):
        uk = UK.objects.get(id=uk)
        requis = {
            "inn": uk.inn,
            "check_acc": uk.ps,
            "bik": uk.bik,
            "corr_acc": uk.ks,
            "bank": uk.bank,
        }
        return requis


    def __str__(self):
        return self.name

    def delete(self):
        self.is_active = False
        self.save()


class House(models.Model):
    city = models.ForeignKey(City, verbose_name="Город", null=True, on_delete=SET_NULL)
    street = models.ForeignKey(Street, verbose_name="Улица", null=True, on_delete=SET_NULL)
    number = models.CharField(verbose_name="Номер", max_length=3)
    add_number = models.CharField(verbose_name="Корпус", max_length=3, blank=True, default="-")
    sq_home = models.DecimalField(verbose_name="Площадь", max_digits=7, decimal_places=2)
    uk = models.ForeignKey(UK, verbose_name="Управляющая компания", null=True, on_delete=SET_NULL)
    category_rate = models.ForeignKey(
        ServicesCategory, verbose_name="Категория", null=True, on_delete=SET_NULL, default=1
    )

    is_active = models.BooleanField(verbose_name="Активный", db_index=True, default=True)
    created = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Обновлен", auto_now=True)

    class Meta:
        verbose_name = "Дом"
        verbose_name_plural = "007 Дома"

    def __str__(self):
        return f"ул.{self.street.street}, д.{self.number}, к.{self.add_number}"

    @staticmethod
    def get_item(house):
        return House.objects.filter(id=house)[0:1]

    def delete(self):
        self.is_active = False
        self.save()


# Общедомовой счетчик (ТЕКУЩИЕ показания)
class HouseCurrent(models.Model):
    period = models.DateField(verbose_name="Создан", default=datetime.datetime.now().replace(day=1))
    house = models.ForeignKey(House, verbose_name="Дом", null=True, on_delete=SET_NULL)
    col_water = models.PositiveIntegerField(verbose_name="Хол.вода", null=True, default=None)
    hot_water = models.PositiveIntegerField(verbose_name="Гор.вода", null=True, default=None)
    electric_day = models.PositiveIntegerField(verbose_name="Электр.день", null=True, default=None)
    electric_night = models.PositiveIntegerField(verbose_name="Электр.ночь", null=True, default=None)

    created = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Обновлен", auto_now=True)

    class Meta:
        verbose_name = "Домовой счетчик (текущий)"
        verbose_name_plural = "Домовые счетчики (текущие)"
        # unique_together = ('house',)

    def __str__(self):
        return f"Период - {self.period}, ул.{self.house.street.street}, Дом №{self.house.number}, к.{self.house.add_number}"

    @staticmethod
    def get_item(user):
        return HouseCurrent.objects.filter(user=user)

    def delete(self):
        self.is_active = False
        self.save()


# Общедомовой счетчик (ИСТОРИЯ показания)
class HouseHistory(models.Model):
    period = models.DateField(verbose_name="Создан", default=datetime.datetime.now().replace(day=1))
    house = models.ForeignKey(House, verbose_name="Дом", null=True, on_delete=SET_NULL)
    col_water = models.PositiveIntegerField(verbose_name="Хол.вода", null=True)
    hot_water = models.PositiveIntegerField(verbose_name="Гор.вода", null=True)
    electric_day = models.PositiveIntegerField(verbose_name="Электр.день", null=True)
    electric_night = models.PositiveIntegerField(verbose_name="Электр.ночь", null=True)

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

    def delete(self):
        self.is_active = False
        self.save()

    # При удалении ловим и сохраняем объект ДОМОВЫЕ ПОКАЗАНИЯ
    @receiver(pre_delete, sender=HouseCurrent)
    def copy_arhive_current_to_history_house(sender, instance, **kwargs):
        house = instance.house_id
        period = instance.period
        upd_val = {
            "col_water": instance.col_water,
            "hot_water": instance.hot_water,
            #TODO электричество пока отменяется
            # "electric_day": instance.electric_day,
            # "electric_night": instance.electric_night,
        }
        obj, created = HouseHistory.objects.update_or_create(house_id=house, period=period, defaults=upd_val)


class Standart(models.Model):
    period = models.DateField(verbose_name="Создан", default=datetime.datetime.now().replace(day=1))
    house = models.ForeignKey(House, verbose_name="Дом", null=True, on_delete=SET_NULL)
    col_water = models.DecimalField(verbose_name="Норматив ХВС", max_digits=6, decimal_places=2)
    hot_water = models.DecimalField(verbose_name="Норматив ХГС", max_digits=6, decimal_places=2)
    electric_day = models.DecimalField(verbose_name="Норматив ЭЛ.День", max_digits=6, decimal_places=2, null=True, default=None)
    electric_night = models.DecimalField(verbose_name="Нориматив ЭЛ.Ночь", max_digits=6, decimal_places=2, null=True, default=None)

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
        return Standart.objects.filter(house=house)[0:1]

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
            "col_water": ((int(instance.col_water) - int(hist.col_water))/sq),
            "hot_water": ((int(instance.hot_water) - int(hist.hot_water))/sq),
            #TODO электричество пока отменяется
            # "electric_day": instance.electric_day,
            # "electric_night": instance.electric_night,
        }
        obj, created = Standart.objects.update_or_create(house_id=house, period=period, defaults=upd_val)


class UserProfile(models.Model):
    SINGLE = "1"
    TWO = "2"
    MULTI = "3"

    MALE = "M"
    FEMALE = "W"

    COUNTER_TYPE = ((SINGLE, "однотарифный"), (TWO, "двухтарифный"))
    GENDER_CHOICES = ((MALE, "М"), (FEMALE, "Ж"))

    user = models.OneToOneField(
        User, verbose_name="Пользоваель", null=False, db_index=True, on_delete=models.CASCADE, related_name="profiles"
    )
    gender = models.CharField(
        verbose_name="Пол", max_length=1, choices=GENDER_CHOICES, blank=True, null=True, default=None
    )
    type_electric_meter = models.CharField(
        verbose_name="Тип счетчика", max_length=1, choices=COUNTER_TYPE, blank=True, null=True, default=None
    )

    is_active = models.BooleanField(verbose_name="Активный", db_index=True, default=True)
    created = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Обновлен", auto_now=True)

    class Meta:
        ordering = ("updated",)
        verbose_name = "Профиль"
        verbose_name_plural = "009 Профили"

    def __str__(self):
        return f'{self.user.personal_account} - {self.user.name} ({"Менеджер" if self.user.is_staff else "Клиент"})'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profiles.save()

    def delete(self):
        self.is_active = False
        self.save()


class Appartament(models.Model):
    user = models.ForeignKey(
        User, verbose_name="Жилец", related_name="appartament", null=True, blank=True, on_delete=SET_NULL
    )
    house = models.ForeignKey(House, verbose_name="Дом", on_delete=CASCADE)
    number = models.CharField(verbose_name="Номер квартиры", max_length=3)
    add_number = models.PositiveIntegerField(verbose_name="Комната", default=0)
    sq_appart = models.DecimalField(
        verbose_name="Площадь", max_digits=5, decimal_places=2, null=True, blank=True, default=0
    )
    num_owner = models.PositiveIntegerField(verbose_name="Кол-во проживающих", null=True, blank=True, default=0)

    is_active = models.BooleanField(verbose_name="Активный", db_index=True, default=True)
    created = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Обновлен", auto_now=True)

    class Meta:
        verbose_name = "Квартира"
        verbose_name_plural = "008 Квартиры"
        unique_together = ("house", "number", "add_number")

    def __str__(self):
        return f"ул.{self.house.street.street}, д.{self.house.number}, кв.{self.number}, комн.{self.add_number}"

    @staticmethod
    def get_item(user):
        return Appartament.objects.filter(user=user)

    def delete(self):
        self.is_active = False
        self.save()


# Текущие показания счетчиков (индивидуальные)
class CurrentCounter(models.Model):
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=CASCADE)
    period = models.DateField(verbose_name="Создан", default=datetime.datetime.now().replace(day=1))
    col_water = models.PositiveIntegerField(verbose_name="Холодная вода", null=True, default=None)
    hot_water = models.PositiveIntegerField(verbose_name="Горячая вода", null=True, default=None)
    electric_day = models.PositiveIntegerField(verbose_name="Электроэнергия день", null=True, blank=True, default=None)
    electric_night = models.PositiveIntegerField(
        verbose_name="Электроэнергия ночь", null=True, blank=True, default=None
    )
    electric_single = models.PositiveIntegerField(
        verbose_name="Электроэнергия", null=True, blank=True, default=None
    )

    created = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Обновлен", auto_now=True)

    class Meta:
        ordering = ("-period",)
        verbose_name = "Индивид. счетчик (текущий)"
        verbose_name_plural = "Индивид. счетчики (текущие)"

    def __str__(self):
        return f"ул.{self.street.street}, д.{self.number}, кв.{self.number}"

    @staticmethod
    def get_last_val(user):
        return CurrentCounter.objects.filter(user=user)[0:1]


# История показания счетчиков (индивидуальные)
class HistoryCounter(models.Model):
    user = models.ForeignKey(User, verbose_name="Пользователь", null=True, on_delete=SET_NULL)
    period = models.DateField(verbose_name="Создан", default=datetime.datetime.now().replace(day=1))
    col_water = models.PositiveIntegerField(verbose_name="Гор.вода", null=True)
    hot_water = models.PositiveIntegerField(verbose_name="Хол.вода", null=True)
    electric_day = models.PositiveIntegerField(verbose_name="Электр.день", null=True, blank=True)
    electric_night = models.PositiveIntegerField(verbose_name="Электр.ночь", null=True, blank=True)
    electric_single = models.PositiveIntegerField(verbose_name="Электр.однотариф", null=True, blank=True)

    created = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Обновлен", auto_now=True)

    class Meta:
        ordering = ("-period",)
        verbose_name = "Индивид. счетчик (история)"
        verbose_name_plural = "Индивид. счетчики (история)"

    @staticmethod
    def get_last_val(user):
        return HistoryCounter.objects.filter(user=user)[0:1]

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
            #TODO электричество пока отменяется
            # "electric_day": instance.electric_day,
            # "electric_night": instance.electric_night,
        }
        obj, created = HistoryCounter.objects.update_or_create(user=user, period=period, defaults=upd_val)


# Перерасчеты
class Recalculations(models.Model):
    user = models.ForeignKey(User, verbose_name="Пользователь", null=True, on_delete=SET_NULL)
    period = models.DateField(verbose_name="Создан", default=datetime.datetime.now().replace(day=1))
    service = models.ForeignKey(Services, verbose_name="Услуга", null=True, on_delete=SET_NULL)
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
        return Recalculations.objects.filter(user=user)[0:1]

    def delete(self):
        self.is_active = False
        self.save()


# Cубсидии
class Subsidies(models.Model):
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=CASCADE)
    service = models.ForeignKey(Services, verbose_name="Услуга", on_delete=CASCADE)
    sale = models.PositiveIntegerField(verbose_name="Субсидии", default=0)
    desc = models.TextField(verbose_name="Описание", blank=True, null=True)

    is_active = models.BooleanField(verbose_name="Активный", db_index=True, default=True)
    created = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Обновлен", auto_now=True)
    desc = models.TextField(verbose_name="Описание", blank=True, null=True)

    class Meta:
        ordering = ("-updated",)
        verbose_name = "Субсидия"
        verbose_name_plural = "010 Субсидии"

    def __str__(self):
        return f"{self.user.user.name} ({self.user.user.personal_account}) - {self.service.name}"

    @staticmethod
    def get_items(user):
        return Subsidies.objects.filter(user=user)

    def delete(self):
        self.is_active = False
        self.save()


# Льготы
class Privileges(models.Model):
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=CASCADE)
    service = models.ForeignKey(Services, verbose_name="Услуга", related_name="service", on_delete=CASCADE)
    sale = models.PositiveIntegerField(verbose_name="Льготы", default=0)
    desc = models.TextField(verbose_name="Описание", blank=True, null=True)

    is_active = models.BooleanField(verbose_name="Активный", db_index=True, default=True)
    created = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Обновлен", auto_now=True)
    desc = models.TextField(verbose_name="Описание", blank=True, null=True)

    class Meta:
        ordering = ("-updated",)
        verbose_name = "Льгота"
        verbose_name_plural = "011 Льготы"

    def __str__(self):
        return f"{self.user.user.name} ({self.user.user.personal_account}) - {self.service.name}"

    @staticmethod
    def get_items(user):
        return Subsidies.objects.filter(user=user)
    
    def delete(self):
        self.is_active = False
        self.save()

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
    total = models.DecimalField(verbose_name="Итого", max_digits=7, decimal_places=2, default=0)
    pre_total = models.DecimalField(verbose_name="Итого", max_digits=7, decimal_places=2, default=0)

    created = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Обновлен", auto_now=True)

    class Meta:
        ordering = ("-period",)
        verbose_name = "Платеж (перепенные)"
        verbose_name_plural = "Платежи (переменные)"

    @staticmethod
    def get_items(user):
        return VariablePayments.objects.filter(user=user)

    @staticmethod
    def get_last_val(user):
        return VariablePayments.objects.filter(user=user)[0:1]

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

    @staticmethod
    def get_items(user):
        return HeaderData.objects.filter(user=user)

    def delete(self):
        self.is_active = False
        self.save()


# Начисления (Плетежка)
class Profit(models.Model):
    user = models.ForeignKey(User, verbose_name="Пользователь", null=True, on_delete=SET_NULL)
    period = models.DateField(verbose_name="Создан", default=datetime.datetime.now().replace(day=1))
    data = JSONField(verbose_name="Данные")
    amount = models.DecimalField(verbose_name="Сумма", max_digits=7, decimal_places=2)

    created = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Обновлен", auto_now=True)

    class Meta:
        ordering = ("-period",)
        verbose_name = "Начисление"
        verbose_name_plural = "Начисления"

    def get_last_val(self):
        return HistoryCounter.objects.filter(user=self.user)[0:1]

    def delete(self):
        self.is_active = False
        self.save()


# Инфорамация по оплатам
class Payment(models.Model):
    user = models.ForeignKey(User, verbose_name="Пользователь", null=True, on_delete=SET_NULL)
    period = models.DateField(verbose_name="Период")
    amount_profit = models.DecimalField(verbose_name="Сумма", max_digits=7, decimal_places=2)

    created = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Обновлен", auto_now=True)

    class Meta:
        ordering = ("-period",)
        verbose_name = "Оплата"
        verbose_name_plural = "Оплаты"

    def get_last_val(self):
        return HistoryCounter.objects.filter(user=self.user)[0:1]

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
    amount = models.DecimalField(verbose_name="Сумма", max_digits=7, decimal_places=2)

    created = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Обновлен", auto_now=True)

    class Meta:
        ordering = ("-period",)
        verbose_name = "Главная книга"
        verbose_name_plural = "Главная книга"

    @staticmethod
    def get_user_debit(user):
        """ Возвращает все поступления на счет конкретного жильца"""
        return MainBook.objects.filter(user = user).filter(direction = 'D')
    
    @staticmethod
    def get_user_credit(user):
        """ Возвращает все списания co счета конкретного жильца"""
        return MainBook.objects.filter(user = user).filter(direction = 'C')

    def get_all_debit():
        """ Возвращает все поступления на счет ВСЕ"""
        return MainBook.objects.filter(direction = 'D')
    
    def get_all_credit():
        """ Возвращает все списания co счета ВСЕ"""
        return MainBook.objects.filter(direction = 'C')

    def delete(self):
        self.is_active = False
        self.save()

    # При изменении константных или переменных расчетов, обновляем сумму начислений
    @receiver(post_save, sender=ConstantPayments)
    @receiver(post_save, sender=VariablePayments)
    def procc_accrual_mainbook(sender, instance, **kwargs):
        user = instance.user
        const_total = ConstantPayments.objects.get(user=user)
        try:
            variable = VariablePayments.get_last_val(user=user)[0]
            period = variable.period
            varia_total = VariablePayments.objects.filter(period=period).get(user=user)
            upd_val = {"amount": (const_total.total + varia_total.total)}
            obj, created = MainBook.objects.update_or_create(user=user, period=period, direction="C", defaults=upd_val)
        except:
            pass


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
        debit = MainBook.get_user_debit(user=user)
        credit = MainBook.get_user_credit(user=user)
        debit_sum = sum(abs(d.amount )for d in debit)
        credit_sum = sum(abs(c.amount) for c in credit)
        upd_val = {
            "amount": (credit_sum - debit_sum),
        }
        obj, created = PersonalAccountStatus.objects.update_or_create(user=user, defaults=upd_val)








