# Generated by Django 2.2.24 on 2021-08-17 19:00

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0025_auto_20210817_1406'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='appartament',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='appartament',
            name='house',
        ),
        migrations.RemoveField(
            model_name='appartament',
            name='user',
        ),
        migrations.RemoveField(
            model_name='house',
            name='category_rate',
        ),
        migrations.RemoveField(
            model_name='house',
            name='city',
        ),
        migrations.RemoveField(
            model_name='house',
            name='street',
        ),
        migrations.DeleteModel(
            name='PostNews',
        ),
        migrations.RemoveField(
            model_name='privileges',
            name='service',
        ),
        migrations.RemoveField(
            model_name='privileges',
            name='user',
        ),
        migrations.RemoveField(
            model_name='services',
            name='category',
        ),
        migrations.RemoveField(
            model_name='services',
            name='unit',
        ),
        migrations.RemoveField(
            model_name='street',
            name='city',
        ),
        migrations.RemoveField(
            model_name='subsidies',
            name='service',
        ),
        migrations.RemoveField(
            model_name='subsidies',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.AlterField(
            model_name='currentcounter',
            name='period',
            field=models.DateField(default=datetime.datetime(2021, 8, 1, 19, 0, 36, 404297), verbose_name='Создан'),
        ),
        migrations.AlterField(
            model_name='historycounter',
            name='period',
            field=models.DateField(default=datetime.datetime(2021, 8, 1, 19, 0, 36, 404831), verbose_name='Создан'),
        ),
        migrations.AlterField(
            model_name='housecurrent',
            name='house',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='directory.House', verbose_name='Дом'),
        ),
        migrations.AlterField(
            model_name='housecurrent',
            name='period',
            field=models.DateField(default=datetime.datetime(2021, 8, 1, 19, 0, 36, 402650), verbose_name='Создан'),
        ),
        migrations.AlterField(
            model_name='househistory',
            name='house',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='directory.House', verbose_name='Дом'),
        ),
        migrations.AlterField(
            model_name='househistory',
            name='period',
            field=models.DateField(default=datetime.datetime(2021, 8, 1, 19, 0, 36, 403151), verbose_name='Создан'),
        ),
        migrations.AlterField(
            model_name='mainbook',
            name='period',
            field=models.DateField(default=datetime.datetime(2021, 8, 1, 19, 0, 36, 407676), verbose_name='Создан'),
        ),
        migrations.AlterField(
            model_name='paymentorder',
            name='period',
            field=models.DateField(default=datetime.datetime(2021, 8, 1, 19, 0, 36, 408386), verbose_name='Создан'),
        ),
        migrations.AlterField(
            model_name='recalculations',
            name='period',
            field=models.DateField(default=datetime.datetime(2021, 8, 1, 19, 0, 36, 405649), verbose_name='Создан'),
        ),
        migrations.AlterField(
            model_name='recalculations',
            name='service',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='directory.Services', verbose_name='Услуга'),
        ),
        migrations.AlterField(
            model_name='standart',
            name='house',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='directory.House', verbose_name='Дом'),
        ),
        migrations.AlterField(
            model_name='standart',
            name='period',
            field=models.DateField(default=datetime.datetime(2021, 8, 1, 19, 0, 36, 403721), verbose_name='Создан'),
        ),
        migrations.AlterField(
            model_name='variablepayments',
            name='period',
            field=models.DateField(default=datetime.datetime(2021, 8, 1, 19, 0, 36, 406696), verbose_name='Создан'),
        ),
        migrations.DeleteModel(
            name='Appartament',
        ),
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='House',
        ),
        migrations.DeleteModel(
            name='Metrics',
        ),
        migrations.DeleteModel(
            name='Privileges',
        ),
        migrations.DeleteModel(
            name='Services',
        ),
        migrations.DeleteModel(
            name='ServicesCategory',
        ),
        migrations.DeleteModel(
            name='Street',
        ),
        migrations.DeleteModel(
            name='Subsidies',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
