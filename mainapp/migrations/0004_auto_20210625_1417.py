# Generated by Django 2.2.24 on 2021-06-25 14:17

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0003_auto_20210625_1045"),
    ]

    operations = [
        migrations.AlterField(
            model_name="currentcounter",
            name="period",
            field=models.DateField(default=datetime.datetime(2021, 6, 1, 14, 17, 44, 215413), verbose_name="Создан"),
        ),
        migrations.AlterField(
            model_name="historycounter",
            name="period",
            field=models.DateField(default=datetime.datetime(2021, 6, 1, 14, 17, 44, 216061), verbose_name="Создан"),
        ),
        migrations.AlterField(
            model_name="housecurrent",
            name="period",
            field=models.DateField(default=datetime.datetime(2021, 6, 1, 14, 17, 44, 211657), verbose_name="Создан"),
        ),
        migrations.AlterField(
            model_name="househistory",
            name="period",
            field=models.DateField(default=datetime.datetime(2021, 6, 1, 14, 17, 44, 212286), verbose_name="Создан"),
        ),
        migrations.AlterField(
            model_name="mainbook",
            name="period",
            field=models.DateField(default=datetime.datetime(2021, 6, 1, 14, 17, 44, 222863), verbose_name="Создан"),
        ),
        migrations.AlterField(
            model_name="profit",
            name="period",
            field=models.DateField(default=datetime.datetime(2021, 6, 1, 14, 17, 44, 221767), verbose_name="Создан"),
        ),
        migrations.AlterField(
            model_name="recalculations",
            name="period",
            field=models.DateField(default=datetime.datetime(2021, 6, 1, 14, 17, 44, 216899), verbose_name="Создан"),
        ),
        migrations.AlterField(
            model_name="standart",
            name="period",
            field=models.DateField(default=datetime.datetime(2021, 6, 1, 14, 17, 44, 213127), verbose_name="Создан"),
        ),
        migrations.AlterField(
            model_name="variablepayments",
            name="period",
            field=models.DateField(default=datetime.datetime(2021, 6, 1, 14, 17, 44, 220636), verbose_name="Создан"),
        ),
    ]
