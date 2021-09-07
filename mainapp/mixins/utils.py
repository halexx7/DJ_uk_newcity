import datetime

from django.core.validators import MinValueValidator
from django.db import models

PERIOD = datetime.datetime.now().replace(day=1)
# PERIOD = datetime.datetime.now().date().replace(day=1, month=11)


class CreateUpdateMixin(models.Model):
    """Примешивает поля даты создания и обновления"""

    created = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Обновлен", auto_now=True)

    class Meta:
        abstract = True


class ActiveMixin(CreateUpdateMixin):
    """Примешивает поле актив, поля создания и обновления"""

    is_active = models.BooleanField(verbose_name="Включено", db_index=True, default=True)

    class Meta:
        abstract = True

    def delete(self):
        self.is_active = False
        self.save()


class WaterCounterMixin(ActiveMixin):
    """Примешивает поля счетчиков холодной и горячей воды"""

    col_water = models.DecimalField(
        verbose_name="Холодная вода",
        null=True,
        default=None,
        max_digits=8,
        decimal_places=3,
        validators=[MinValueValidator(0.001)],
    )
    hot_water = models.DecimalField(
        verbose_name="Горячая вода",
        null=True,
        default=None,
        max_digits=8,
        decimal_places=3,
        validators=[MinValueValidator(0.001)],
    )

    class Meta:
        abstract = True


class ElectroCounterMixin(ActiveMixin):
    """Примешивает поля счетчков электроэнергии"""

    electric_day = models.DecimalField(
        verbose_name="Электроэнергия день",
        null=True,
        default=None,
        max_digits=8,
        decimal_places=3,
        validators=[MinValueValidator(0.001)],
    )
    electric_night = models.DecimalField(
        verbose_name="Электоэнергия ночь",
        null=True,
        default=None,
        max_digits=8,
        decimal_places=3,
        validators=[MinValueValidator(0.001)],
    )
    electric_single = models.DecimalField(
        verbose_name="Электроэнергия",
        null=True,
        default=None,
        max_digits=8,
        decimal_places=3,
        validators=[MinValueValidator(0.001)],
    )

    class Meta:
        abstract = True
