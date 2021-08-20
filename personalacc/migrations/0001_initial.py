# Generated by Django 2.2.24 on 2021-08-17 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="SiteConfiguration",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(help_text="УК Новый город", max_length=128, verbose_name="Название")),
                ("city", models.CharField(help_text="г.Тюмень", max_length=128, verbose_name="Город")),
                ("street", models.CharField(help_text="ул.Свободы", max_length=256, verbose_name="Улица")),
                ("num_building", models.CharField(help_text="д.5", max_length=5, verbose_name="Номер здания")),
                (
                    "phone",
                    models.CharField(
                        blank=True,
                        help_text="Номер телефона в формате - 79823212334",
                        max_length=11,
                        null=True,
                        verbose_name="Телефон",
                    ),
                ),
                ("email", models.EmailField(help_text="info@uk.ru", max_length=254, verbose_name="e-mail")),
                ("inn", models.CharField(help_text="1533455446", max_length=10, verbose_name="ИНН")),
                (
                    "ps",
                    models.CharField(help_text="48800939999000393949", max_length=20, verbose_name="Расчетный счет"),
                ),
                ("bik", models.CharField(help_text="1009089074", max_length=10, verbose_name="БИК")),
                ("ks", models.CharField(help_text="38700939999000393949", max_length=20, verbose_name="Кор.счет")),
                ("bank", models.CharField(help_text='ОАО "Cбербанк"', max_length=128, verbose_name="Банк")),
                ("web_addr", models.CharField(help_text="www.uk-newcity.ru", max_length=128, verbose_name="Сайт")),
                (
                    "key_ya",
                    models.CharField(
                        blank=True,
                        help_text="1888f9f3-1174-48c4-b1b4-fa129bй2345234",
                        max_length=128,
                        verbose_name="Api-ключ Яндекса",
                    ),
                ),
                ("lat", models.CharField(blank=True, help_text="57.167979", max_length=64, verbose_name="Широта")),
                ("lon", models.CharField(blank=True, help_text="65.564430", max_length=64, verbose_name="Долгота")),
                (
                    "footer_copyright",
                    models.CharField(
                        blank=True,
                        default="Все права защищены © Тюмень 2015 - 2021 гг.",
                        max_length=256,
                        verbose_name="Футер копирайт",
                    ),
                ),
                ("is_active", models.BooleanField(db_index=True, default=True, verbose_name="Активный")),
                ("created", models.DateTimeField(auto_now_add=True, verbose_name="Создан")),
                ("updated", models.DateTimeField(auto_now=True, verbose_name="Обновлен")),
            ],
            options={
                "verbose_name": "Настройки сайта",
            },
        ),
    ]
