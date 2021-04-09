# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    personal_account = models.CharField(max_length=128, help_text="Введите номер лицевого счета", verbose_name="Лицевой счет", unique=True)
    password = models.CharField(verbose_name="Пароль", max_length=128)

    first_name = models.CharField(verbose_name="Имя", max_length=30, blank=True)
    last_name = models.CharField(verbose_name="Фамилия", max_length=30, blank=True)
    patronymic = models.CharField(verbose_name="Отчество", max_length=30, blank=True)

    email = models.EmailField(verbose_name="Email", unique=True)
    is_active = models.BooleanField(verbose_name="Активный", default=True)
    is_staff = models.BooleanField(default=True, verbose_name="Доступ к админке")
    is_superuser = models.BooleanField(default=False, verbose_name='Суперпользователь', help_text='Обозначает, что у этого пользователя есть все разрешения, без их явного назначения.')

    last_login = models.DateTimeField(blank=True, null=True, verbose_name='Последний вход')

    objects = UserManager()

    USERNAME_FIELD = 'personal_account'
    REQUIRED_FIELDS = ['password', 'email']

    class Meta:
        verbose_name = _('Пользователь')
        verbose_name_plural = _('Пользователи')

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name plus patronymic, with a space in between.
        '''
        full_name = f'{self.last_name} {self.first_name} {self.patronymic}'
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)