from django.conf import settings
from django.urls import re_path

import invoice.views as invoice
from invoice.apps import InvoiceConfig

app_name = InvoiceConfig.name

urlpatterns = [
    re_path(r"^invoice/(?P<pk>\d+)/$", invoice.InvoiceViews.as_view(), name="invoice"),
]

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns()
