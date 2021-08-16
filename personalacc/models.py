from django.db import models
from solo.models import SingletonModel

from mainapp.models import City, Street

class SiteConfiguration(SingletonModel):
    name = models.CharField(verbose_name="Название", max_length=128, help_text="УК Новый город")
    city = models.CharField(verbose_name="Город", max_length=128, help_text="г.Тюмень")
    street = models.CharField(verbose_name="Улица", max_length=256, help_text="ул.Свободы")
    num_building = models.CharField(verbose_name="Номер здания", max_length=5, help_text="д.5")
    phone = models.CharField(
        verbose_name="Телефон", max_length=11, null=True, blank=True, help_text="Номер телефона в формате - 79823212334"
    )
    email = models.EmailField(verbose_name="e-mail", help_text="info@uk.ru")
    inn = models.CharField(verbose_name="ИНН", max_length=10, help_text="1533455446")
    ps = models.CharField(verbose_name="Расчетный счет", max_length=20, help_text="48800939999000393949")
    bik = models.CharField(verbose_name="БИК", max_length=10, help_text="1009089074")
    ks = models.CharField(verbose_name="Кор.счет", max_length=20, help_text="38700939999000393949")
    bank = models.CharField(verbose_name="Банк", max_length=128, help_text="ОАО \"Cбербанк\"")
    web_addr = models.CharField(verbose_name="Сайт", max_length=128, help_text="www.uk-newcity.ru")

    key_ya = models.CharField(verbose_name="Api-ключ Яндекса", max_length=128, blank=True, help_text="1888f9f3-1174-48c4-b1b4-fa129bй2345234")
    lat = models.CharField(verbose_name="Широта", max_length=64, blank=True, help_text="57.167979")
    lon = models.CharField(verbose_name="Долгота", max_length=64, blank=True, help_text="65.564430")

    footer_copyright = models.CharField(
        max_length=256, blank=True, default="Все права защищены © Тюмень 2015 - 2021 гг.", verbose_name="Футер копирайт"
    )

    is_active = models.BooleanField(verbose_name="Активный", db_index=True, default=True)
    created = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Обновлен", auto_now=True)

    def get_full_name(self):
        name = {
            "name": self.name,
            "address": f"{self.street}, {self.num_building}",
            "phone": f"{self.phone}",
            "web": self.web_addr,
        }
        return name

    def get_requisites(self):
        requis = {
            "inn": self.inn,
            "check_acc": self.ps,
            "bik": self.bik,
            "corr_acc": self.ks,
            "bank": self.bank,
        }
        return requis

    def __str__(self):
        return "Настройки сайта"

    class Meta:
        verbose_name = "Настройки сайта"
