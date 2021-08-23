# Generated by Django 2.2.24 on 2021-08-22 21:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0014_auto_20210822_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='averageсalculationbuffer',
            name='period',
            field=models.DateField(default=datetime.datetime(2021, 8, 1, 21, 40, 53, 585335), verbose_name='Период'),
        ),
        migrations.AlterField(
            model_name='currentcounter',
            name='period',
            field=models.DateField(default=datetime.datetime(2021, 8, 1, 21, 40, 53, 579351), verbose_name='Период'),
        ),
        migrations.AlterField(
            model_name='historycounter',
            name='period',
            field=models.DateField(default=datetime.datetime(2021, 8, 1, 21, 40, 53, 580005), verbose_name='Период'),
        ),
        migrations.AlterField(
            model_name='housecurrent',
            name='period',
            field=models.DateField(default=datetime.datetime(2021, 8, 1, 21, 40, 53, 577435), verbose_name='Период'),
        ),
        migrations.AlterField(
            model_name='househistory',
            name='period',
            field=models.DateField(default=datetime.datetime(2021, 8, 1, 21, 40, 53, 577982), verbose_name='Период'),
        ),
        migrations.AlterField(
            model_name='mainbook',
            name='period',
            field=models.DateField(default=datetime.datetime(2021, 8, 1, 21, 40, 53, 583045), verbose_name='Период'),
        ),
        migrations.AlterField(
            model_name='paymentorder',
            name='period',
            field=models.DateField(default=datetime.datetime(2021, 8, 1, 21, 40, 53, 583986), verbose_name='Период'),
        ),
        migrations.AlterField(
            model_name='recalculations',
            name='period',
            field=models.DateField(default=datetime.datetime(2021, 8, 1, 21, 40, 53, 580627), verbose_name='Период'),
        ),
        migrations.AlterField(
            model_name='standart',
            name='period',
            field=models.DateField(default=datetime.datetime(2021, 8, 1, 21, 40, 53, 578596), verbose_name='Период'),
        ),
        migrations.AlterField(
            model_name='variablepayments',
            name='period',
            field=models.DateField(default=datetime.datetime(2021, 8, 1, 21, 40, 53, 581859), verbose_name='Период'),
        ),
    ]
