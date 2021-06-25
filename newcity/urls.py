from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path

import mainapp.views as mainapp

urlpatterns = [
    re_path(r"^$", mainapp.IndexList.as_view(), name="main"),
    re_path(r"^contact/$", mainapp.ContactList.as_view(), name="contact"),
    # path("", mainapp.main, name="main"),
    path("auth/", include("authnapp.urls", namespace="auth")),
    path("person/", include("personalacc.urls", namespace="person")),
    path("directory/", include("directory.urls", namespace="directory")),
    path("invoice/", include("invoice.urls", namespace="invoice")),
    path("admin/", admin.site.urls, name="admin"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
