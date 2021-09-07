# Generated by Django 2.2.24 on 2021-08-23 21:00

import datetime

from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ("authnapp", "0013_auto_20210821_2019"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="activation_key_expires",
            field=models.DateTimeField(
                default=datetime.datetime(2021, 8, 25, 21, 0, 26, 8853, tzinfo=utc), verbose_name="Актуальность ключа"
            ),
        ),
    ]
