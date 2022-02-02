from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import re_path

import apps.mainapp.views as mainapp

urlpatterns = [
    re_path(r"^$", mainapp.IndexList.as_view(), name="main"),
    re_path(r"^contact/$", mainapp.ContactList.as_view(), name="contact"),
    re_path(r"^news/$", mainapp.NewstList.as_view(), name="news"),
    re_path(r"^auth/", include("apps.authnapp.urls", namespace="auth")),
    re_path(r"^directory/", include("apps.directory.urls", namespace="directory")),
    re_path(r"^person/", include("apps.personalacc.urls", namespace="person")),
    re_path(r"^invoice/", include("apps.invoice.urls", namespace="invoice")),
    re_path(r"^admin/", admin.site.urls, name="admin"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
