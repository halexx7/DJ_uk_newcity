# Generated by Django 2.2.24 on 2021-08-17 22:10

import datetime

from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ("authnapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="activation_key_expires",
            field=models.DateTimeField(
                default=datetime.datetime(2021, 8, 19, 22, 10, 12, 7455, tzinfo=utc), verbose_name="Актуальность ключа"
            ),
        ),
    ]
