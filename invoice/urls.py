from django.conf import settings
from django.urls import re_path, path
import invoice.views as invoice
from invoice.apps import InvoiceConfig

app_name = InvoiceConfig.name

urlpatterns = [
    re_path(r"^$", invoice.InvoiceViews.as_view(), name="invoice"),
    # path('invoice/', invoice.main, name='invoice'),
]

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()