# Generated by Django 2.2.24 on 2021-08-21 20:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authnapp', '0012_auto_20210821_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 23, 20, 19, 11, 566541, tzinfo=utc), verbose_name='Актуальность ключа'),
        ),
    ]
