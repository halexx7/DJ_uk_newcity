# Generated by Django 2.2.24 on 2021-08-15 18:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authnapp', '0012_auto_20210814_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 17, 18, 59, 55, 112958, tzinfo=utc), verbose_name='Актуальность ключа'),
        ),
    ]
