# Generated by Django 2.2.24 on 2021-08-14 21:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authnapp', '0011_auto_20210814_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 16, 21, 34, 17, 600054, tzinfo=utc), verbose_name='Актуальность ключа'),
        ),
    ]
