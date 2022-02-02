from django.core.validators import MinValueValidator
from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.authnapp.models import User
from apps.mainapp.mixins.utils import ActiveMixin


class PostNews(ActiveMixin):
    title = models.CharField(verbose_name="Заголовок", max_length=128)
    content = models.TextField(verbose_name="Описание")

    class Meta:
        ordering = ("-created",)
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def __str__(self):
        return f"{self.title} - ({self.updated})"

    @staticmethod
    def get_items():
        return PostNews.objects.filter(is_active=True)


class ServicesCategory(ActiveMixin):
    name = models.CharField(verbose_name="Название", max_length=32)

    class Meta:
        verbose_name = "Категория услуг"
        verbose_name_plural = "006 Категории услуг"

    def __str__(self):
        return self.name


class Metrics(ActiveMixin):
    name = models.CharField(verbose_name="Единица измерения", max_length=32)

    class Meta:
        verbose_name = "Единица измерения"
        verbose_name_plural = "005 Единицы измерения"

    def __str__(self):
        return self.name


class Services(ActiveMixin):
    category = models.ForeignKey(
        ServicesCategory, verbose_name="Категория", related_name="category", on_delete=models.CASCADE, default=1
    )
    name = models.CharField(verbose_name="Услуга", max_length=256)
    unit = models.ForeignKey(Metrics, verbose_name="Единицы", related_name="unit", on_delete=models.CASCADE)
    rate = models.DecimalField(
        verbose_name="Тариф", max_digits=7, decimal_places=3, default=0, validators=[MinValueValidator(0.001)]
    )
    factor = models.DecimalField(
        verbose_name="Коэфициент", max_digits=3, decimal_places=2, default=1, validators=[MinValueValidator(0.01)]
    )
    const = models.BooleanField(verbose_name="Константа", db_index=True, default=True)

    class Meta:
        verbose_name = "Услугу"
        verbose_name_plural = "007 Услуги"

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


class City(ActiveMixin):
    city = models.CharField(verbose_name="Город", max_length=128)

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "001 Города"

    def __str__(self):
        return self.city


class Street(ActiveMixin):
    city = models.ForeignKey(City, verbose_name="Город", on_delete=CASCADE)
    street = models.CharField(verbose_name="Улица", max_length=128)

    class Meta:
        verbose_name = "Улица"
        verbose_name_plural = "002 Улицы"

    def __str__(self):
        return f"ул.{self.street}"


class House(ActiveMixin):
    city = models.ForeignKey(City, verbose_name="Город", null=True, on_delete=SET_NULL)
    street = models.ForeignKey(Street, verbose_name="Улица", null=True, on_delete=SET_NULL)
    number = models.DecimalField(
        verbose_name="Номер", max_digits=3, decimal_places=0, validators=[MinValueValidator(0)]
    )
    add_number = models.CharField(verbose_name="Корпус", max_length=3, blank=True, default="-")
    sq_home = models.DecimalField(
        verbose_name="Площадь", max_digits=7, decimal_places=2, validators=[MinValueValidator(0.01)]
    )
    category_rate = models.ForeignKey(
        ServicesCategory, verbose_name="Категория", null=True, on_delete=SET_NULL, default=1
    )

    class Meta:
        ordering = ("-updated",)
        verbose_name = "Дом"
        verbose_name_plural = "003 Дома"

    def __str__(self):
        return f"ул.{self.street.street}, д.{self.number}, к.{self.add_number}"

    @staticmethod
    def get_item(house):
        return House.objects.filter(id=house)[0:1]


class UserProfile(ActiveMixin):
    MALE = "M"
    FEMALE = "W"
    GENDER_CHOICES = ((MALE, "М"), (FEMALE, "Ж"))

    user = models.OneToOneField(
        User, verbose_name="Пользоваель", null=False, db_index=True, on_delete=models.CASCADE, related_name="profiles"
    )
    gender = models.CharField(
        verbose_name="Пол", max_length=1, choices=GENDER_CHOICES, blank=True, null=True, default=None
    )

    class Meta:
        ordering = ("updated",)
        verbose_name = "Профиль"
        verbose_name_plural = "008 Профили"

    def __str__(self):
        return f'{self.user.personal_account} - {self.user.name} ({"Менеджер" if self.user.is_staff else "Клиент"})'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profiles.save()


class Appartament(ActiveMixin):
    user = models.ForeignKey(
        User, verbose_name="Жилец", related_name="appartament", null=True, blank=True, on_delete=SET_NULL
    )
    house = models.ForeignKey(House, verbose_name="Дом", on_delete=CASCADE)
    number = models.DecimalField(
        verbose_name="Номер квартиры",
        max_digits=3,
        decimal_places=0,
        null=True,
        blank=True,
        default=0,
        validators=[MinValueValidator(0)],
    )
    add_number = models.DecimalField(
        verbose_name="Комната",
        max_digits=3,
        decimal_places=0,
        null=True,
        blank=True,
        default=0,
        validators=[MinValueValidator(0)],
    )
    sq_appart = models.DecimalField(
        verbose_name="Площадь",
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True,
        default=0,
        validators=[MinValueValidator(0.01)],
    )
    num_owner = models.PositiveIntegerField(verbose_name="Кол-во проживающих", null=True, blank=True, default=0)

    class Meta:
        verbose_name = "Квартира"
        verbose_name_plural = "004 Квартиры"
        unique_together = ("house", "number", "add_number")

    def __str__(self):
        return f"ул.{self.house.street.street}, д.{self.house.number}, кв.{self.number}, комн.{self.add_number}"

    @staticmethod
    def get_item(user):
        return Appartament.objects.filter(user=user)


# Cубсидии
class Subsidies(ActiveMixin):
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=CASCADE)
    service = models.ForeignKey(Services, verbose_name="Услуга", on_delete=CASCADE)
    sale = models.PositiveIntegerField(verbose_name="Субсидии", default=0)
    desc = models.TextField(verbose_name="Описание", blank=True, null=True)

    class Meta:
        ordering = ("-updated",)
        verbose_name = "Субсидия"
        verbose_name_plural = "009 Субсидии"

    def __str__(self):
        return f"{self.user.user.name} ({self.user.user.personal_account}) - {self.service.name}"

    @staticmethod
    def get_items(user):
        return Subsidies.objects.filter(user=user)

    @staticmethod
    def get_qty_last_items(qty):
        return Subsidies.objects.all()[:qty]


# Льготы
class Privileges(ActiveMixin):
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=CASCADE)
    service = models.ForeignKey(Services, verbose_name="Услуга", related_name="service", on_delete=CASCADE)
    sale = models.PositiveIntegerField(verbose_name="Льготы", default=0)
    desc = models.TextField(verbose_name="Описание", blank=True, null=True)

    class Meta:
        ordering = ("-updated",)
        verbose_name = "Льгота"
        verbose_name_plural = "010 Льготы"

    def __str__(self):
        return f"{self.user.user.name} ({self.user.user.personal_account}) - {self.service.name}"

    @staticmethod
    def get_items(user):
        return Privileges.objects.filter(user=user)

    @staticmethod
    def get_qty_last_items(qty):
        return Privileges.objects.all()[:qty]
