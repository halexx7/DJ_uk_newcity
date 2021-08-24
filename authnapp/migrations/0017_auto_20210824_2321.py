# Generated by Django 2.2.24 on 2021-08-24 23:21

import datetime
import django.core.validators
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authnapp', '0016_merge_20210823_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 26, 23, 21, 2, 581995, tzinfo=utc), verbose_name='Актуальность ключа'),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(blank=True, help_text='Иванов Иван Иванович', max_length=128, null=True, validators=[django.core.validators.RegexValidator('^[a-zA-Zа-яА-ЯёЁ]*$', 'Cпециальные символы и цифры не допускаются!'), django.core.validators.MinLengthValidator(2), django.core.validators.MaxLengthValidator(128)], verbose_name='ФИО'),
        ),
        migrations.AlterField(
            model_name='user',
            name='personal_account',
            field=models.CharField(help_text='Введите номер лицевого счета: 777777', max_length=128, unique=True, validators=[django.core.validators.RegexValidator('\\d', 'Лицевой счет состоит только из цифр!'), django.core.validators.MinLengthValidator(6, 'Лицевой счет состоит из 6 цифр. Вы ввели меньше.'), django.core.validators.MaxLengthValidator(6, 'Лицевой счет состоит из 6 цифр. Вы ввели больше.')], verbose_name='Лицевой счет'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, help_text='Номер телефона в формате - 79823212334', max_length=11, null=True, validators=[django.core.validators.RegexValidator('\\d{6}', 'Телефон состоит только из цифр!'), django.core.validators.MinLengthValidator(11, 'Телефон состоит из 11 цифр. Вы ввели меньше.'), django.core.validators.MaxLengthValidator(11, 'Телефон состоит из 11 цифр. Вы ввели больше.')], verbose_name='Телефон'),
        ),
    ]
