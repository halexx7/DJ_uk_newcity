# Generated by Django 2.2.24 on 2021-09-07 19:24

import datetime

from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ("authnapp", "0017_auto_20210824_2321"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="activation_key_expires",
            field=models.DateTimeField(
                default=datetime.datetime(2021, 9, 9, 19, 24, 16, 96783, tzinfo=utc), verbose_name="Актуальность ключа"
            ),
        ),
    ]
