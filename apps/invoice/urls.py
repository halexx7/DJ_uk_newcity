from django.conf import settings
from django.urls import path, re_path

import apps.invoice.views as invoice
from apps.invoice.apps import InvoiceConfig

app_name = InvoiceConfig.name

urlpatterns = [
    re_path(r"^invoice/(?P<pk>\d+)/$", invoice.InvoiceViews.as_view(), name="invoice"),
    # path('invoice/', invoice.main, name='invoice'),
]

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns()
