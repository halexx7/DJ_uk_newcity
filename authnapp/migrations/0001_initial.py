# Generated by Django 2.2.24 on 2021-06-15 11:43

import datetime

from django.db import migrations, models
from django.utils.timezone import utc

import authnapp.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0011_update_proxy_permissions"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("is_client", models.BooleanField(default=True, verbose_name="Пользователь")),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Обозначает, что этот пользователь - Администратор",
                        verbose_name="Менеджер",
                    ),
                ),
                (
                    "personal_account",
                    models.CharField(
                        help_text="Введите номер лицевого счета: 7777777",
                        max_length=128,
                        unique=True,
                        verbose_name="Лицевой счет",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="Пароль")),
                (
                    "name",
                    models.CharField(
                        blank=True, help_text="Иванов Иван Иванович", max_length=128, null=True, verbose_name="ФИО"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True,
                        help_text="E-mail в формате - user@example.com",
                        max_length=254,
                        null=True,
                        unique=True,
                        verbose_name="Email",
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        blank=True,
                        help_text="Номер телефона в формате - 79823212334",
                        max_length=11,
                        null=True,
                        verbose_name="Телефон",
                    ),
                ),
                ("is_active", models.BooleanField(default=True, verbose_name="Активный")),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Обозначает, что у этого пользователя есть все разрешения, без их явного назначения.",
                        verbose_name="Суперпользователь",
                    ),
                ),
                ("last_login", models.DateTimeField(blank=True, null=True, verbose_name="Последний вход")),
                ("activation_key", models.CharField(blank=True, max_length=128, verbose_name="Ключ подтверждения")),
                (
                    "activation_key_expires",
                    models.DateTimeField(
                        default=datetime.datetime(2021, 6, 17, 11, 43, 10, 715426, tzinfo=utc),
                        verbose_name="Актуальность ключа",
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.Group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.Permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "Пользователь",
                "verbose_name_plural": "Пользователи",
            },
            managers=[
                ("objects", authnapp.managers.UserManager()),
            ],
        ),
    ]
