# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import timedelta

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import Group, PermissionsMixin
from django.core.mail import send_mail
from django.core.validators import (MaxLengthValidator, MinLengthValidator,
                                    RegexValidator)
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    is_client = models.BooleanField(
        default=True, verbose_name="Пользователь", help_text="Если это житель поставьте галку."
    )
    is_staff = models.BooleanField(
        default=False, verbose_name="Менеджер", help_text="Обозначает, что этот пользователь - Администратор"
    )
    personal_account = models.CharField(
        max_length=128,
        verbose_name="Лицевой счет",
        unique=True,
        help_text="Введите номер лицевого счета: 777777",
        validators=[
            RegexValidator(r"^\d", "Лицевой счет состоит только из цифр!"),
            MinLengthValidator(6, "Лицевой счет состоит из 6 цифр. Вы ввели меньше."),
            MaxLengthValidator(6, "Лицевой счет состоит из 6 цифр. Вы ввели больше."),
        ],
    )
    password = models.CharField(verbose_name="Пароль", max_length=128)
    name = models.CharField(
        verbose_name="ФИО",
        max_length=128,
        null=True,
        blank=True,
        help_text="Иванов Иван Иванович",
        validators=[
            RegexValidator(r"^[a-zA-Zа-яА-ЯёЁ ]*$", "Cпециальные символы и цифры не допускаются!"),
            MinLengthValidator(2),
            MaxLengthValidator(128),
        ],
    )
    email = models.EmailField(
        verbose_name="Email", unique=True, null=True, blank=True, help_text="E-mail в формате - user@example.com"
    )
    phone = models.CharField(
        verbose_name="Телефон",
        max_length=11,
        null=True,
        blank=True,
        help_text="Номер телефона в формате - 79823212334",
        validators=[
            RegexValidator(r"\d{11}", "Телефон должен состоять только из цифр!"),
            MinLengthValidator(11, "Телефон состоит из 11 цифр. Вы ввели меньше."),
            MaxLengthValidator(11, "Телефон состоит из 11 цифр. Вы ввели больше."),
        ],
    )
    is_active = models.BooleanField(verbose_name="Активный", default=True)
    is_superuser = models.BooleanField(
        default=False,
        verbose_name="Суперпользователь",
        help_text="Обозначает, что у этого пользователя есть все разрешения, без их явного назначения.",
    )
    last_login = models.DateTimeField(blank=True, null=True, verbose_name="Последний вход")
    activation_key = models.CharField(verbose_name="Ключ подтверждения", max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(
        verbose_name="Актуальность ключа", default=(now() + timedelta(hours=48))
    )
    objects = UserManager()

    USERNAME_FIELD = "personal_account"
    REQUIRED_FIELDS = ["password", "email"]

    class Meta:
        verbose_name = _("Пользователь")
        verbose_name_plural = _("Пользователи")

    def __str__(self):
        return f"({self.personal_account}) - {self.name}"

    def get_full_name(self):
        full_name = f"{self.name}"
        return full_name.strip()

    def get_short_name(self):
        return self.name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this User"""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def is_activation_key_expired(self):
        """Checks if the key is up-to-date."""
        if now() <= self.activation_key_expires:
            return False
        else:
            return True


# Подсели на сигнал после сохранения модели
@receiver(post_save, sender=User)
def add_admin_permission(sender, instance, created, **kwargs):
    if created and not instance.is_superuser:
        if instance.is_client:
            # Если клиент добавляем в группу "Client"
            grupo = Group.objects.get(name="Client")
            grupo.user_set.add(instance)
        if instance.is_staff:
            # Если Менеджер очищаем от всех групп и добавляем в группу "Manager"
            instance.groups.clear()
            grupo = Group.objects.get(name="Manager")
            grupo.user_set.add(instance)
