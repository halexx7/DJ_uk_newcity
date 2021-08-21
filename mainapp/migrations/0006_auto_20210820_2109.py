# Generated by Django 2.2.24 on 2021-08-20 21:09

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_auto_20210820_1953'),
    ]

    operations = [
        migrations.AddField(
            model_name='constantpayments',
            name='is_active',
            field=models.BooleanField(db_index=True, default=True, verbose_name='Включено'),
        ),
        migrations.AddField(
            model_name='currentcounter',
            name='is_active',
            field=models.BooleanField(db_index=True, default=True, verbose_name='Включено'),
        ),
        migrations.AddField(
            model_name='historycounter',
            name='is_active',
            field=models.BooleanField(db_index=True, default=True, verbose_name='Включено'),
        ),
        migrations.AddField(
            model_name='housecurrent',
            name='is_active',
            field=models.BooleanField(db_index=True, default=True, verbose_name='Включено'),
        ),
        migrations.AddField(
            model_name='househistory',
            name='is_active',
            field=models.BooleanField(db_index=True, default=True, verbose_name='Включено'),
        ),
        migrations.AddField(
            model_name='mainbook',
            name='is_active',
            field=models.BooleanField(db_index=True, default=True, verbose_name='Включено'),
        ),
        migrations.AddField(
            model_name='paymentorder',
            name='is_active',
            field=models.BooleanField(db_index=True, default=True, verbose_name='Включено'),
        ),
        migrations.AddField(
            model_name='recalculations',
            name='is_active',
            field=models.BooleanField(db_index=True, default=True, verbose_name='Включено'),
        ),
        migrations.AddField(
            model_name='standart',
            name='is_active',
            field=models.BooleanField(db_index=True, default=True, verbose_name='Включено'),
        ),
        migrations.AddField(
            model_name='variablepayments',
            name='is_active',
            field=models.BooleanField(db_index=True, default=True, verbose_name='Включено'),
        ),
        migrations.AlterField(
            model_name='averageсalculationbuffer',
            name='col_water',
            field=models.DecimalField(decimal_places=3, default=None, max_digits=10, null=True, verbose_name='Буффер холодной воды'),
        ),
        migrations.AlterField(
            model_name='averageсalculationbuffer',
            name='hot_water',
            field=models.DecimalField(decimal_places=3, default=None, max_digits=10, null=True, verbose_name='Буффер горячей воды'),
        ),
        migrations.AlterField(
            model_name='averageсalculationbuffer',
            name='sewage',
            field=models.DecimalField(decimal_places=3, default=None, max_digits=10, null=True, verbose_name='Буффер сточных вод'),
        ),
        migrations.AlterField(
            model_name='currentcounter',
            name='col_water',
            field=models.DecimalField(decimal_places=3, default=None, max_digits=8, null=True, validators=[django.core.validators.MinValueValidator(0.001)], verbose_name='Холодная вода'),
        ),
        migrations.AlterField(
            model_name='currentcounter',
            name='hot_water',
            field=models.DecimalField(decimal_places=3, default=None, max_digits=8, null=True, validators=[django.core.validators.MinValueValidator(0.001)], verbose_name='Горячая вода'),
        ),
        migrations.AlterField(
            model_name='currentcounter',
            name='period',
            field=models.DateField(default=datetime.datetime(2021, 8, 1, 21, 9, 16, 677862), verbose_name='Создан'),
        ),
        migrations.AlterField(
            model_name='historycounter',
            name='col_water',
            field=models.DecimalField(decimal_places=3, default=None, max_digits=8, null=True, validators=[django.core.validators.MinValueValidator(0.001)], verbose_name='Холодная вода'),
        ),
        migrations.AlterField(
            model_name='historycounter',
            name='hot_water',
            field=models.DecimalField(decimal_places=3, default=None, max_digits=8, null=True, validators=[django.core.validators.MinValueValidator(0.001)], verbose_name='Горячая вода'),
        ),
        migrations.AlterField(
            model_name='historycounter',
            name='period',
            field=models.DateField(default=datetime.datetime(2021, 8, 1, 21, 9, 16, 678463), verbose_name='Создан'),
        ),
        migrations.AlterField(
            model_name='housecurrent',
            name='col_water',
            field=models.DecimalField(decimal_places=3, default=None, max_digits=8, null=True, validators=[django.core.validators.MinValueValidator(0.001)], verbose_name='Холодная вода'),
        ),
        migrations.AlterField(
            model_name='housecurrent',
            name='hot_water',
            field=models.DecimalField(decimal_places=3, default=None, max_digits=8, null=True, validators=[django.core.validators.MinValueValidator(0.001)], verbose_name='Горячая вода'),
        ),
        migrations.AlterField(
            model_name='housecurrent',
            name='period',
            field=models.DateField(default=datetime.datetime(2021, 8, 1, 21, 9, 16, 675919), verbose_name='Создан'),
        ),
        migrations.AlterField(
            model_name='househistory',
            name='col_water',
            field=models.DecimalField(decimal_places=3, default=None, max_digits=8, null=True, validators=[django.core.validators.MinValueValidator(0.001)], verbose_name='Холодная вода'),
        ),
        migrations.AlterField(
            model_name='househistory',
            name='hot_water',
            field=models.DecimalField(decimal_places=3, default=None, max_digits=8, null=True, validators=[django.core.validators.MinValueValidator(0.001)], verbose_name='Горячая вода'),
        ),
        migrations.AlterField(
            model_name='househistory',
            name='period',
            field=models.DateField(default=datetime.datetime(2021, 8, 1, 21, 9, 16, 676670), verbose_name='Создан'),
        ),
        migrations.AlterField(
            model_name='mainbook',
            name='period',
            field=models.DateField(default=datetime.datetime(2021, 8, 1, 21, 9, 16, 681151), verbose_name='Создан'),
        ),
        migrations.AlterField(
            model_name='paymentorder',
            name='period',
            field=models.DateField(default=datetime.datetime(2021, 8, 1, 21, 9, 16, 682067), verbose_name='Создан'),
        ),
        migrations.AlterField(
            model_name='recalculations',
            name='period',
            field=models.DateField(default=datetime.datetime(2021, 8, 1, 21, 9, 16, 679038), verbose_name='Создан'),
        ),
        migrations.AlterField(
            model_name='standart',
            name='period',
            field=models.DateField(default=datetime.datetime(2021, 8, 1, 21, 9, 16, 677249), verbose_name='Создан'),
        ),
        migrations.AlterField(
            model_name='variablepayments',
            name='period',
            field=models.DateField(default=datetime.datetime(2021, 8, 1, 21, 9, 16, 680159), verbose_name='Создан'),
        ),
    ]
