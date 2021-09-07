# Generated by Django 2.2.24 on 2021-08-20 21:09

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0006_auto_20210820_2109"),
    ]

    operations = [
        migrations.AlterField(
            model_name="currentcounter",
            name="period",
            field=models.DateField(default=datetime.datetime(2021, 8, 1, 21, 9, 44, 194125), verbose_name="Создан"),
        ),
        migrations.AlterField(
            model_name="historycounter",
            name="period",
            field=models.DateField(default=datetime.datetime(2021, 8, 1, 21, 9, 44, 194643), verbose_name="Создан"),
        ),
        migrations.AlterField(
            model_name="housecurrent",
            name="period",
            field=models.DateField(default=datetime.datetime(2021, 8, 1, 21, 9, 44, 192309), verbose_name="Создан"),
        ),
        migrations.AlterField(
            model_name="househistory",
            name="period",
            field=models.DateField(default=datetime.datetime(2021, 8, 1, 21, 9, 44, 192864), verbose_name="Создан"),
        ),
        migrations.AlterField(
            model_name="mainbook",
            name="period",
            field=models.DateField(default=datetime.datetime(2021, 8, 1, 21, 9, 44, 197593), verbose_name="Создан"),
        ),
        migrations.AlterField(
            model_name="paymentorder",
            name="period",
            field=models.DateField(default=datetime.datetime(2021, 8, 1, 21, 9, 44, 198315), verbose_name="Создан"),
        ),
        migrations.AlterField(
            model_name="recalculations",
            name="period",
            field=models.DateField(default=datetime.datetime(2021, 8, 1, 21, 9, 44, 195230), verbose_name="Создан"),
        ),
        migrations.AlterField(
            model_name="standart",
            name="period",
            field=models.DateField(default=datetime.datetime(2021, 8, 1, 21, 9, 44, 193481), verbose_name="Создан"),
        ),
        migrations.AlterField(
            model_name="variablepayments",
            name="period",
            field=models.DateField(default=datetime.datetime(2021, 8, 1, 21, 9, 44, 196572), verbose_name="Создан"),
        ),
    ]
