# Generated by Django 2.2.24 on 2021-08-21 19:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authnapp', '0009_auto_20210821_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 23, 19, 50, 18, 701901, tzinfo=utc), verbose_name='Актуальность ключа'),
        ),
    ]
