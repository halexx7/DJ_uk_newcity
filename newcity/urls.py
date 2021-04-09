from django.urls import path
from django.contrib import admin
import mainapp.views as mainapp

urlpatterns = [
    path('', mainapp.main),
    # path('products/', mainapp.products),
    # path('contact/', mainapp.contact),
    # path('admin/', admin.site.urls),
]
