# Generated by Django 2.2.24 on 2021-08-15 21:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0016_auto_20210815_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currentcounter',
            name='period',
            field=models.DateField(default=datetime.datetime(2021, 8, 1, 21, 15, 8, 476944), verbose_name='Создан'),
        ),
        migrations.AlterField(
            model_name='historycounter',
            name='period',
            field=models.DateField(default=datetime.datetime(2021, 8, 1, 21, 15, 8, 477568), verbose_name='Создан'),
        ),
        migrations.AlterField(
            model_name='housecurrent',
            name='period',
            field=models.DateField(default=datetime.datetime(2021, 8, 1, 21, 15, 8, 471539), verbose_name='Создан'),
        ),
        migrations.AlterField(
            model_name='househistory',
            name='period',
            field=models.DateField(default=datetime.datetime(2021, 8, 1, 21, 15, 8, 472094), verbose_name='Создан'),
        ),
        migrations.AlterField(
            model_name='mainbook',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Сумма'),
        ),
        migrations.AlterField(
            model_name='mainbook',
            name='period',
            field=models.DateField(default=datetime.datetime(2021, 8, 1, 21, 15, 8, 482750), verbose_name='Создан'),
        ),
        migrations.AlterField(
            model_name='paymentorder',
            name='period',
            field=models.DateField(default=datetime.datetime(2021, 8, 1, 21, 15, 8, 483604), verbose_name='Создан'),
        ),
        migrations.AlterField(
            model_name='recalculations',
            name='period',
            field=models.DateField(default=datetime.datetime(2021, 8, 1, 21, 15, 8, 478407), verbose_name='Создан'),
        ),
        migrations.AlterField(
            model_name='standart',
            name='period',
            field=models.DateField(default=datetime.datetime(2021, 8, 1, 21, 15, 8, 472740), verbose_name='Создан'),
        ),
        migrations.AlterField(
            model_name='variablepayments',
            name='period',
            field=models.DateField(default=datetime.datetime(2021, 8, 1, 21, 15, 8, 481029), verbose_name='Создан'),
        ),
    ]
