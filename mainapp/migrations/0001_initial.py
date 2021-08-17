# Generated by Django 2.2.24 on 2021-08-17 21:12

import datetime
from django.conf import settings
import django.contrib.postgres.fields.jsonb
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('directory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VariablePayments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.DateField(default=datetime.datetime(2021, 8, 1, 21, 12, 0, 388445), verbose_name='Создан')),
                ('data', django.contrib.postgres.fields.jsonb.JSONField(verbose_name='data')),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Итого')),
                ('pre_total', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Итого')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Платеж (перепенные)',
                'verbose_name_plural': 'Платежи (переменные)',
                'ordering': ('-period',),
            },
        ),
        migrations.CreateModel(
            name='Standart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.DateField(default=datetime.datetime(2021, 8, 1, 21, 12, 0, 385304), verbose_name='Создан')),
                ('col_water', models.DecimalField(decimal_places=6, max_digits=11, verbose_name='Норматив ХВС')),
                ('hot_water', models.DecimalField(decimal_places=6, max_digits=11, verbose_name='Норматив ХГС')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
                ('house', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='directory.House', verbose_name='Дом')),
            ],
            options={
                'verbose_name': 'Норматив',
                'verbose_name_plural': 'Нормативы',
                'ordering': ('-period',),
            },
        ),
        migrations.CreateModel(
            name='Recalculations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.DateField(default=datetime.datetime(2021, 8, 1, 21, 12, 0, 387288), verbose_name='Создан')),
                ('recalc', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Сумма')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='directory.Services', verbose_name='Услуга')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Перерасчет',
                'verbose_name_plural': 'Перерасчеты',
                'ordering': ('-updated',),
            },
        ),
        migrations.CreateModel(
            name='PersonalAccountStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Состояние')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Состояние счета',
                'verbose_name_plural': 'Состояния счетов',
                'ordering': ('amount',),
            },
        ),
        migrations.CreateModel(
            name='PaymentOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.DateField(default=datetime.datetime(2021, 8, 1, 21, 12, 0, 390189), verbose_name='Создан')),
                ('header_data', django.contrib.postgres.fields.jsonb.JSONField(default=None, null=True, verbose_name='Данные для шапки')),
                ('constant_data', django.contrib.postgres.fields.jsonb.JSONField(verbose_name='Постоянная часть')),
                ('variable_data', django.contrib.postgres.fields.jsonb.JSONField(verbose_name='Переменная часть')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Чистая_сумма')),
                ('pre_amount', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Грязная сумма')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Начисление',
                'verbose_name_plural': 'Начисления',
                'ordering': ('-period',),
            },
        ),
        migrations.CreateModel(
            name='MainBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.DateField(default=datetime.datetime(2021, 8, 1, 21, 12, 0, 389443), verbose_name='Создан')),
                ('direction', models.CharField(choices=[('D', 'Оплата'), ('C', 'Начисление')], max_length=1, verbose_name='Направление')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Сумма')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Главная книга',
                'verbose_name_plural': 'Главная книга',
                'ordering': ('-period',),
            },
        ),
        migrations.CreateModel(
            name='HouseHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.DateField(default=datetime.datetime(2021, 8, 1, 21, 12, 0, 384644), verbose_name='Создан')),
                ('col_water', models.DecimalField(decimal_places=3, max_digits=8, null=True, validators=[django.core.validators.MinValueValidator(0.001)], verbose_name='Хол.вода')),
                ('hot_water', models.DecimalField(decimal_places=3, max_digits=8, null=True, validators=[django.core.validators.MinValueValidator(0.001)], verbose_name='Гор.вода')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
                ('house', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='directory.House', verbose_name='Дом')),
            ],
            options={
                'verbose_name': 'Домовой счетчик (история)',
                'verbose_name_plural': 'Домовые счетчики (история)',
                'ordering': ('-updated',),
            },
        ),
        migrations.CreateModel(
            name='HouseCurrent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.DateField(default=datetime.datetime(2021, 8, 1, 21, 12, 0, 384016), verbose_name='Создан')),
                ('col_water', models.DecimalField(decimal_places=3, default=None, max_digits=8, null=True, validators=[django.core.validators.MinValueValidator(0.001)], verbose_name='Хол.вода')),
                ('hot_water', models.DecimalField(decimal_places=3, default=None, max_digits=8, null=True, validators=[django.core.validators.MinValueValidator(0.001)], verbose_name='Гор.вода')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
                ('house', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='directory.House', verbose_name='Дом')),
            ],
            options={
                'verbose_name': 'Домовой счетчик (текущий)',
                'verbose_name_plural': 'Домовые счетчики (текущие)',
                'ordering': ('-updated',),
            },
        ),
        migrations.CreateModel(
            name='HistoryCounter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.DateField(default=datetime.datetime(2021, 8, 1, 21, 12, 0, 386529), verbose_name='Создан')),
                ('col_water', models.DecimalField(decimal_places=3, max_digits=8, null=True, validators=[django.core.validators.MinValueValidator(0.001)], verbose_name='Хол.вода')),
                ('hot_water', models.DecimalField(decimal_places=3, max_digits=8, null=True, validators=[django.core.validators.MinValueValidator(0.001)], verbose_name='Гор.вода')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Индивид. счетчик (история)',
                'verbose_name_plural': 'Индивид. счетчики (история)',
                'ordering': ('-period',),
            },
        ),
        migrations.CreateModel(
            name='HeaderData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', django.contrib.postgres.fields.jsonb.JSONField(verbose_name='Данные')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Начисление',
                'verbose_name_plural': 'Начисления',
            },
        ),
        migrations.CreateModel(
            name='CurrentCounter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.DateField(default=datetime.datetime(2021, 8, 1, 21, 12, 0, 385934), verbose_name='Создан')),
                ('col_water', models.DecimalField(decimal_places=3, max_digits=8, null=True, validators=[django.core.validators.MinValueValidator(0.001)], verbose_name='Хол.вода')),
                ('hot_water', models.DecimalField(decimal_places=3, max_digits=8, null=True, validators=[django.core.validators.MinValueValidator(0.001)], verbose_name='Гор.вода')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Индивид. счетчик (текущий)',
                'verbose_name_plural': 'Индивид. счетчики (текущие)',
                'ordering': ('-period',),
            },
        ),
        migrations.CreateModel(
            name='ConstantPayments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', django.contrib.postgres.fields.jsonb.JSONField(verbose_name='data')),
                ('total', models.DecimalField(decimal_places=3, max_digits=8, verbose_name='Сумма')),
                ('pre_total', models.DecimalField(decimal_places=3, max_digits=8, verbose_name='Сумма')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Платеж (постоянные)',
                'verbose_name_plural': 'Платежи (постоянные)',
            },
        ),
        migrations.CreateModel(
            name='AverageСalculationBuffer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('col_water', models.DecimalField(decimal_places=2, default=None, max_digits=10, null=True, verbose_name='Буффер холодной воды')),
                ('hot_water', models.DecimalField(decimal_places=2, default=None, max_digits=10, null=True, verbose_name='Буффер горячей воды')),
                ('sewage', models.DecimalField(decimal_places=2, default=None, max_digits=10, null=True, verbose_name='Буффер сточных вод')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Буффер средних начислений',
            },
        ),
    ]
