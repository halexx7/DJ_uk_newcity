from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from django.utils import timezone
from celery.schedules import crontab

REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'newcity.settings')

app = Celery('newcity', backend='redis', broker='redis://{REDIS_HOST}:6379/1')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
app.now = timezone.now
