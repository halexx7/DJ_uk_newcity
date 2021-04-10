from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

import mainapp.views as mainapp

urlpatterns = [
    path("", mainapp.main, name="main"),
    path("auth/", include("authnapp.urls", namespace="auth")),
    # path('products/', mainapp.products),
    # path('contact/', mainapp.contact),
    path("admin/", admin.site.urls, name="admin"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
