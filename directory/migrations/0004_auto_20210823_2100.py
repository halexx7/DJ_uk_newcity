# Generated by Django 2.2.24 on 2021-08-23 21:00

import django.core.validators
from django.db import migrations, models

import mainapp.mixins.validator


class Migration(migrations.Migration):

    dependencies = [
        ("directory", "0003_auto_20210820_2109"),
    ]

    operations = [
        migrations.AlterField(
            model_name="appartament",
            name="add_number",
            field=models.CharField(
                default=0,
                max_length=3,
                validators=[mainapp.mixins.validator.check_value_is_digit],
                verbose_name="Комната",
            ),
        ),
        migrations.AlterField(
            model_name="appartament",
            name="number",
            field=models.CharField(
                max_length=3, validators=[mainapp.mixins.validator.check_value_is_digit], verbose_name="Номер квартиры"
            ),
        ),
        migrations.AlterField(
            model_name="appartament",
            name="sq_appart",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                default=0,
                max_digits=5,
                null=True,
                validators=[django.core.validators.MinValueValidator(0.01)],
                verbose_name="Площадь",
            ),
        ),
        migrations.AlterField(
            model_name="house",
            name="number",
            field=models.CharField(
                max_length=3, validators=[django.core.validators.MinValueValidator(1)], verbose_name="Номер"
            ),
        ),
        migrations.AlterField(
            model_name="house",
            name="sq_home",
            field=models.DecimalField(
                decimal_places=2,
                max_digits=7,
                validators=[django.core.validators.MinValueValidator(0.01)],
                verbose_name="Площадь",
            ),
        ),
        migrations.AlterField(
            model_name="services",
            name="factor",
            field=models.DecimalField(
                decimal_places=2,
                default=1,
                max_digits=3,
                validators=[django.core.validators.MinValueValidator(0.01)],
                verbose_name="Коэфициент",
            ),
        ),
    ]
