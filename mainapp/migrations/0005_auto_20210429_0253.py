# Generated by Django 2.2.17 on 2021-04-29 02:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_auto_20210429_0251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='housecurrent',
            name='period',
            field=models.DateField(default=datetime.datetime(2021, 4, 1, 2, 53, 55, 651740), verbose_name='Создан'),
        ),
        migrations.AlterField(
            model_name='househistory',
            name='period',
            field=models.DateField(default=datetime.datetime(2021, 4, 1, 2, 53, 55, 652512), verbose_name='Создан'),
        ),
        migrations.AlterUniqueTogether(
            name='appartament',
            unique_together={('house', 'number', 'add_number')},
        ),
    ]