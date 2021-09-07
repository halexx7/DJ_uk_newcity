# Generated by Django 2.2.24 on 2021-08-23 21:00

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0013_auto_20210821_2019"),
    ]

    operations = [
        migrations.AlterField(
            model_name="averageсalculationbuffer",
            name="period",
            field=models.DateField(default=datetime.datetime(2021, 8, 1, 21, 0, 26, 35395), verbose_name="Период"),
        ),
        migrations.AlterField(
            model_name="currentcounter",
            name="period",
            field=models.DateField(default=datetime.datetime(2021, 8, 1, 21, 0, 26, 29810), verbose_name="Период"),
        ),
        migrations.AlterField(
            model_name="historycounter",
            name="period",
            field=models.DateField(default=datetime.datetime(2021, 8, 1, 21, 0, 26, 30399), verbose_name="Период"),
        ),
        migrations.AlterField(
            model_name="housecurrent",
            name="period",
            field=models.DateField(default=datetime.datetime(2021, 8, 1, 21, 0, 26, 28086), verbose_name="Период"),
        ),
        migrations.AlterField(
            model_name="househistory",
            name="period",
            field=models.DateField(default=datetime.datetime(2021, 8, 1, 21, 0, 26, 28590), verbose_name="Период"),
        ),
        migrations.AlterField(
            model_name="mainbook",
            name="period",
            field=models.DateField(default=datetime.datetime(2021, 8, 1, 21, 0, 26, 33282), verbose_name="Период"),
        ),
        migrations.AlterField(
            model_name="paymentorder",
            name="period",
            field=models.DateField(default=datetime.datetime(2021, 8, 1, 21, 0, 26, 34074), verbose_name="Период"),
        ),
        migrations.AlterField(
            model_name="recalculations",
            name="period",
            field=models.DateField(default=datetime.datetime(2021, 8, 1, 21, 0, 26, 31019), verbose_name="Период"),
        ),
        migrations.AlterField(
            model_name="standart",
            name="period",
            field=models.DateField(default=datetime.datetime(2021, 8, 1, 21, 0, 26, 29209), verbose_name="Период"),
        ),
        migrations.AlterField(
            model_name="variablepayments",
            name="period",
            field=models.DateField(default=datetime.datetime(2021, 8, 1, 21, 0, 26, 32188), verbose_name="Период"),
        ),
    ]
