# Generated by Django 2.2.17 on 2021-04-26 02:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authnapp', '0002_auto_20210423_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 28, 2, 25, 43, 978958, tzinfo=utc), verbose_name='Актуальность ключа'),
        ),
    ]
