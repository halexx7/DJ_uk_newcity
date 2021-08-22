# Generated by Django 2.2.24 on 2021-08-20 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0002_remove_userprofile_type_electric_meter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appartament',
            name='is_active',
            field=models.BooleanField(db_index=True, default=True, verbose_name='Включено'),
        ),
        migrations.AlterField(
            model_name='city',
            name='is_active',
            field=models.BooleanField(db_index=True, default=True, verbose_name='Включено'),
        ),
        migrations.AlterField(
            model_name='house',
            name='is_active',
            field=models.BooleanField(db_index=True, default=True, verbose_name='Включено'),
        ),
        migrations.AlterField(
            model_name='metrics',
            name='is_active',
            field=models.BooleanField(db_index=True, default=True, verbose_name='Включено'),
        ),
        migrations.AlterField(
            model_name='postnews',
            name='is_active',
            field=models.BooleanField(db_index=True, default=True, verbose_name='Включено'),
        ),
        migrations.AlterField(
            model_name='privileges',
            name='is_active',
            field=models.BooleanField(db_index=True, default=True, verbose_name='Включено'),
        ),
        migrations.AlterField(
            model_name='services',
            name='is_active',
            field=models.BooleanField(db_index=True, default=True, verbose_name='Включено'),
        ),
        migrations.AlterField(
            model_name='servicescategory',
            name='is_active',
            field=models.BooleanField(db_index=True, default=True, verbose_name='Включено'),
        ),
        migrations.AlterField(
            model_name='street',
            name='is_active',
            field=models.BooleanField(db_index=True, default=True, verbose_name='Включено'),
        ),
        migrations.AlterField(
            model_name='subsidies',
            name='is_active',
            field=models.BooleanField(db_index=True, default=True, verbose_name='Включено'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='is_active',
            field=models.BooleanField(db_index=True, default=True, verbose_name='Включено'),
        ),
    ]