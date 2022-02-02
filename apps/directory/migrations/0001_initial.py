# Generated by Django 2.2.24 on 2022-02-02 22:07

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
                ('is_active', models.BooleanField(db_index=True, default=True, verbose_name='Включено')),
                ('city', models.CharField(max_length=128, verbose_name='Город')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': '001 Города',
            },
        ),
        migrations.CreateModel(
            name='Metrics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
                ('is_active', models.BooleanField(db_index=True, default=True, verbose_name='Включено')),
                ('name', models.CharField(max_length=32, verbose_name='Единица измерения')),
            ],
            options={
                'verbose_name': 'Единица измерения',
                'verbose_name_plural': '005 Единицы измерения',
            },
        ),
        migrations.CreateModel(
            name='PostNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
                ('is_active', models.BooleanField(db_index=True, default=True, verbose_name='Включено')),
                ('title', models.CharField(max_length=128, verbose_name='Заголовок')),
                ('content', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
                ('is_active', models.BooleanField(db_index=True, default=True, verbose_name='Включено')),
                ('name', models.CharField(max_length=256, verbose_name='Услуга')),
                ('rate', models.DecimalField(decimal_places=3, default=0, max_digits=7, validators=[django.core.validators.MinValueValidator(0.001)], verbose_name='Тариф')),
                ('factor', models.DecimalField(decimal_places=2, default=1, max_digits=3, validators=[django.core.validators.MinValueValidator(0.01)], verbose_name='Коэфициент')),
                ('const', models.BooleanField(db_index=True, default=True, verbose_name='Константа')),
            ],
            options={
                'verbose_name': 'Услугу',
                'verbose_name_plural': '007 Услуги',
            },
        ),
        migrations.CreateModel(
            name='ServicesCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
                ('is_active', models.BooleanField(db_index=True, default=True, verbose_name='Включено')),
                ('name', models.CharField(max_length=32, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Категория услуг',
                'verbose_name_plural': '006 Категории услуг',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
                ('is_active', models.BooleanField(db_index=True, default=True, verbose_name='Включено')),
                ('gender', models.CharField(blank=True, choices=[('M', 'М'), ('W', 'Ж')], default=None, max_length=1, null=True, verbose_name='Пол')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profiles', to=settings.AUTH_USER_MODEL, verbose_name='Пользоваель')),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': '008 Профили',
                'ordering': ('updated',),
            },
        ),
        migrations.CreateModel(
            name='Subsidies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
                ('is_active', models.BooleanField(db_index=True, default=True, verbose_name='Включено')),
                ('sale', models.PositiveIntegerField(default=0, verbose_name='Субсидии')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='directory.Services', verbose_name='Услуга')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Субсидия',
                'verbose_name_plural': '009 Субсидии',
                'ordering': ('-updated',),
            },
        ),
        migrations.CreateModel(
            name='Street',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
                ('is_active', models.BooleanField(db_index=True, default=True, verbose_name='Включено')),
                ('street', models.CharField(max_length=128, verbose_name='Улица')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='directory.City', verbose_name='Город')),
            ],
            options={
                'verbose_name': 'Улица',
                'verbose_name_plural': '002 Улицы',
            },
        ),
        migrations.AddField(
            model_name='services',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='directory.ServicesCategory', verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='services',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='unit', to='directory.Metrics', verbose_name='Единицы'),
        ),
        migrations.CreateModel(
            name='Privileges',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
                ('is_active', models.BooleanField(db_index=True, default=True, verbose_name='Включено')),
                ('sale', models.PositiveIntegerField(default=0, verbose_name='Льготы')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service', to='directory.Services', verbose_name='Услуга')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Льгота',
                'verbose_name_plural': '010 Льготы',
                'ordering': ('-updated',),
            },
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
                ('is_active', models.BooleanField(db_index=True, default=True, verbose_name='Включено')),
                ('number', models.DecimalField(decimal_places=0, max_digits=3, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Номер')),
                ('add_number', models.CharField(blank=True, default='-', max_length=3, verbose_name='Корпус')),
                ('sq_home', models.DecimalField(decimal_places=2, max_digits=7, validators=[django.core.validators.MinValueValidator(0.01)], verbose_name='Площадь')),
                ('category_rate', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='directory.ServicesCategory', verbose_name='Категория')),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='directory.City', verbose_name='Город')),
                ('street', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='directory.Street', verbose_name='Улица')),
            ],
            options={
                'verbose_name': 'Дом',
                'verbose_name_plural': '003 Дома',
                'ordering': ('-updated',),
            },
        ),
        migrations.CreateModel(
            name='Appartament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
                ('is_active', models.BooleanField(db_index=True, default=True, verbose_name='Включено')),
                ('number', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=3, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Номер квартиры')),
                ('add_number', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=3, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Комната')),
                ('sq_appart', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True, validators=[django.core.validators.MinValueValidator(0.01)], verbose_name='Площадь')),
                ('num_owner', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Кол-во проживающих')),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='directory.House', verbose_name='Дом')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='appartament', to=settings.AUTH_USER_MODEL, verbose_name='Жилец')),
            ],
            options={
                'verbose_name': 'Квартира',
                'verbose_name_plural': '004 Квартиры',
                'unique_together': {('house', 'number', 'add_number')},
            },
        ),
    ]
