# Generated by Django 2.2.24 on 2021-08-14 21:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0011_auto_20210814_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currentcounter',
            name='period',
            field=models.DateField(default=datetime.datetime(2021, 8, 1, 21, 34, 17, 610112), verbose_name='Создан'),
        ),
        migrations.AlterField(
            model_name='historycounter',
            name='period',
            field=models.DateField(default=datetime.datetime(2021, 8, 1, 21, 34, 17, 611782), verbose_name='Создан'),
        ),
        migrations.AlterField(
            model_name='housecurrent',
            name='period',
            field=models.DateField(default=datetime.datetime(2021, 8, 1, 21, 34, 17, 606778), verbose_name='Создан'),
        ),
        migrations.AlterField(
            model_name='househistory',
            name='period',
            field=models.DateField(default=datetime.datetime(2021, 8, 1, 21, 34, 17, 607371), verbose_name='Создан'),
        ),
        migrations.AlterField(
            model_name='mainbook',
            name='period',
            field=models.DateField(default=datetime.datetime(2021, 8, 1, 21, 34, 17, 616377), verbose_name='Создан'),
        ),
        migrations.AlterField(
            model_name='paymentorder',
            name='period',
            field=models.DateField(default=datetime.datetime(2021, 8, 1, 21, 34, 17, 617070), verbose_name='Создан'),
        ),
        migrations.AlterField(
            model_name='recalculations',
            name='period',
            field=models.DateField(default=datetime.datetime(2021, 8, 1, 21, 34, 17, 612452), verbose_name='Создан'),
        ),
        migrations.AlterField(
            model_name='standart',
            name='period',
            field=models.DateField(default=datetime.datetime(2021, 8, 1, 21, 34, 17, 608075), verbose_name='Создан'),
        ),
        migrations.AlterField(
            model_name='variablepayments',
            name='period',
            field=models.DateField(default=datetime.datetime(2021, 8, 1, 21, 34, 17, 614882), verbose_name='Создан'),
        ),
    ]
