# Generated by Django 2.2.24 on 2022-03-04 14:17

import datetime
from django.conf import settings
import django.contrib.postgres.fields.jsonb
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('directory', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='VariablePayments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
                ('is_active', models.BooleanField(db_index=True, default=True, verbose_name='Включено')),
                ('period', models.DateField(default=datetime.datetime(2022, 3, 1, 14, 17, 24, 194652), verbose_name='Период')),
                ('data', django.contrib.postgres.fields.jsonb.JSONField(verbose_name='data')),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Итого')),
                ('pre_total', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Итого')),
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
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
                ('is_active', models.BooleanField(db_index=True, default=True, verbose_name='Включено')),
                ('period', models.DateField(default=datetime.datetime(2022, 3, 1, 14, 17, 24, 191128), verbose_name='Период')),
                ('col_water', models.DecimalField(decimal_places=6, max_digits=11, verbose_name='Норматив ХВС')),
                ('hot_water', models.DecimalField(decimal_places=6, max_digits=11, verbose_name='Норматив ХГС')),
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
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
                ('is_active', models.BooleanField(db_index=True, default=True, verbose_name='Включено')),
                ('period', models.DateField(default=datetime.datetime(2022, 3, 1, 14, 17, 24, 192748), verbose_name='Период')),
                ('recalc', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Сумма')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('is_auto', models.BooleanField(default=False, verbose_name='Автоматический')),
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
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Состояние')),
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
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
                ('is_active', models.BooleanField(db_index=True, default=True, verbose_name='Включено')),
                ('period', models.DateField(default=datetime.datetime(2022, 3, 1, 14, 17, 24, 196230), verbose_name='Период')),
                ('header_data', django.contrib.postgres.fields.jsonb.JSONField(default=None, null=True, verbose_name='Данные для шапки')),
                ('constant_data', django.contrib.postgres.fields.jsonb.JSONField(verbose_name='Постоянная часть')),
                ('variable_data', django.contrib.postgres.fields.jsonb.JSONField(verbose_name='Переменная часть')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Чистая_сумма')),
                ('pre_amount', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Грязная сумма')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Платежка)',
                'verbose_name_plural': '(Платежка)',
                'ordering': ('-period',),
            },
        ),
        migrations.CreateModel(
            name='MainBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
                ('is_active', models.BooleanField(db_index=True, default=True, verbose_name='Включено')),
                ('period', models.DateField(default=datetime.datetime(2022, 3, 1, 14, 17, 24, 195592), verbose_name='Период')),
                ('direction', models.CharField(choices=[('D', 'Оплата'), ('C', 'Начисление')], max_length=1, verbose_name='Направление')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Сумма')),
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
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
                ('is_active', models.BooleanField(db_index=True, default=True, verbose_name='Включено')),
                ('col_water', models.DecimalField(decimal_places=3, default=None, max_digits=8, null=True, validators=[django.core.validators.MinValueValidator(0.001)], verbose_name='Холодная вода')),
                ('hot_water', models.DecimalField(decimal_places=3, default=None, max_digits=8, null=True, validators=[django.core.validators.MinValueValidator(0.001)], verbose_name='Горячая вода')),
                ('period', models.DateField(default=datetime.datetime(2022, 3, 1, 14, 17, 24, 190567), verbose_name='Период')),
                ('house', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='directory.House', verbose_name='Дом')),
            ],
            options={
                'verbose_name': 'Домовой счетчик (история)',
                'verbose_name_plural': '01 Домовые счетчики (история)',
                'ordering': ('-updated',),
            },
        ),
        migrations.CreateModel(
            name='HouseCurrent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
                ('is_active', models.BooleanField(db_index=True, default=True, verbose_name='Включено')),
                ('col_water', models.DecimalField(decimal_places=3, default=None, max_digits=8, null=True, validators=[django.core.validators.MinValueValidator(0.001)], verbose_name='Холодная вода')),
                ('hot_water', models.DecimalField(decimal_places=3, default=None, max_digits=8, null=True, validators=[django.core.validators.MinValueValidator(0.001)], verbose_name='Горячая вода')),
                ('period', models.DateField(default=datetime.datetime(2022, 3, 1, 14, 17, 24, 190078), verbose_name='Период')),
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
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
                ('is_active', models.BooleanField(db_index=True, default=True, verbose_name='Включено')),
                ('col_water', models.DecimalField(decimal_places=3, default=None, max_digits=8, null=True, validators=[django.core.validators.MinValueValidator(0.001)], verbose_name='Холодная вода')),
                ('hot_water', models.DecimalField(decimal_places=3, default=None, max_digits=8, null=True, validators=[django.core.validators.MinValueValidator(0.001)], verbose_name='Горячая вода')),
                ('period', models.DateField(default=datetime.datetime(2022, 3, 1, 14, 17, 24, 192199), verbose_name='Период')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Индивидуальный счетчик (история)',
                'verbose_name_plural': '02 Индивидуальные счетчики (история)',
                'ordering': ('-period',),
            },
        ),
        migrations.CreateModel(
            name='HeaderData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
                ('data', django.contrib.postgres.fields.jsonb.JSONField(verbose_name='Данные')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': '(Платежка) данные шапки',
                'verbose_name_plural': '(Платежка) данные шапок',
            },
        ),
        migrations.CreateModel(
            name='CurrentCounter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
                ('is_active', models.BooleanField(db_index=True, default=True, verbose_name='Включено')),
                ('col_water', models.DecimalField(decimal_places=3, default=None, max_digits=8, null=True, validators=[django.core.validators.MinValueValidator(0.001)], verbose_name='Холодная вода')),
                ('hot_water', models.DecimalField(decimal_places=3, default=None, max_digits=8, null=True, validators=[django.core.validators.MinValueValidator(0.001)], verbose_name='Горячая вода')),
                ('period', models.DateField(default=datetime.datetime(2022, 3, 1, 14, 17, 24, 191716), verbose_name='Период')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Индивидуальный счетчик (текущий)',
                'verbose_name_plural': 'Индивидуальные счетчики (текущие)',
                'ordering': ('-period',),
            },
        ),
        migrations.CreateModel(
            name='ConstantPayments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
                ('is_active', models.BooleanField(db_index=True, default=True, verbose_name='Включено')),
                ('data', django.contrib.postgres.fields.jsonb.JSONField(verbose_name='data')),
                ('total', models.DecimalField(decimal_places=3, max_digits=8, verbose_name='Сумма')),
                ('pre_total', models.DecimalField(decimal_places=3, max_digits=8, verbose_name='Сумма')),
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
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
                ('period', models.DateField(default=datetime.datetime(2022, 3, 1, 14, 17, 24, 197542), verbose_name='Период')),
                ('col_water', models.DecimalField(decimal_places=3, default=None, max_digits=10, null=True, verbose_name='Буффер холодной воды')),
                ('hot_water', models.DecimalField(decimal_places=3, default=None, max_digits=10, null=True, verbose_name='Буффер горячей воды')),
                ('sewage', models.DecimalField(decimal_places=3, default=None, max_digits=10, null=True, verbose_name='Буффер сточных вод')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Буффер средних начислений',
                'unique_together': {('user', 'period')},
            },
        ),
    ]
