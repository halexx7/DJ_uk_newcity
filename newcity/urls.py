from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

import apps.mainapp.views as mainapp

urlpatterns = [
    path("", mainapp.IndexList.as_view(), name="main"),
    path("contact/", mainapp.ContactList.as_view(), name="contact"),
    path("news/", mainapp.NewstList.as_view(), name="news"),
    path("auth/", include("apps.authnapp.urls", namespace="auth")),
    path("directory/", include("apps.directory.urls", namespace="directory")),
    path("person/", include("apps.personalacc.urls", namespace="person")),
    path("invoice/", include("apps.invoice.urls", namespace="invoice")),
    path("admin/", admin.site.urls, name="admin"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
