# Generated by Django 2.2.24 on 2021-06-25 10:45

import datetime

from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ("authnapp", "0002_auto_20210616_0249"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="activation_key_expires",
            field=models.DateTimeField(
                default=datetime.datetime(2021, 6, 27, 10, 45, 44, 966689, tzinfo=utc),
                verbose_name="Актуальность ключа",
            ),
        ),
    ]
