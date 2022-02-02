from django.contrib import admin
from import_export import resources
from solo.admin import SingletonModelAdmin

from apps.personalacc.models import SiteConfiguration

admin.site.register(SiteConfiguration, SingletonModelAdmin)


#Import-Export
class SiteConfigurationResource(resources.ModelResource):
    class Meta:
        model = SiteConfiguration
