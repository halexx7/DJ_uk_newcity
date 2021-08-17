from django.contrib import admin

# from authnapp.models import User
from directory.models import (
    Appartament,
    City,
    House,
    Metrics,
    PostNews,
    Privileges,
    Services,
    ServicesCategory,
    Street,
    Subsidies,
    UserProfile,
)


class ServicesInline(admin.TabularInline):
    model = Services

    def get_extra(self, request, obj=None, **kwargs):
        """Hook for customizing the number of extra inline forms."""
        self.extra = 0
        return self.extra


class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "updated")
    search_fields = [
        "name",
    ]
    list_filter = (
        "created",
        "updated",
    )
    inlines = [ServicesInline,]


class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "updated")
    search_fields = [
        "name",
    ]
    list_filter = (
        "category",
        "created",
        "updated",
    )


class StreetInline(admin.TabularInline):
    model = Street

    def get_extra(self, request, obj=None, **kwargs):
        """Hook for customizing the number of extra inline forms."""
        self.extra = 1
        return self.extra


class CityAdmin(admin.ModelAdmin):
    list_display = ("city", "updated")
    search_fields = [
        "city",
    ]
    list_filter = (
        "created",
        "updated",
    )
    inlines = [
        StreetInline,
    ]


class HouseInline(admin.TabularInline):
    model = House

    def get_extra(self, request, obj=None, **kwargs):
        """Hook for customizing the number of extra inline forms."""
        self.extra = 0
        return self.extra


class StreetAdmin(admin.ModelAdmin):
    list_display = ("city", "street", "number", "updated")
    search_fields = ["city", "street", "number"]
    list_filter = (
        "city",
        "street",
        "created",
        "updated",
    )
    inlines = [HouseInline,]


class AppartamentInline(admin.TabularInline):
    model = Appartament

    def get_extra(self, request, obj=None, **kwargs):
        """Hook for customizing the number of extra inline forms."""
        self.extra = 0
        return self.extra


class HouseAdmin(admin.ModelAdmin):
    list_display = ("city", "street", "number", "updated")
    search_fields = ["city", "street", "number"]
    list_filter = (
        "city",
        "street",
        "created",
        "updated",
    )
    inlines = [AppartamentInline,]


# USERPROFILES
class SubsidiesInline(admin.TabularInline):
    model = Subsidies

    def get_extra(self, request, obj=None, **kwargs):
        """Hook for customizing the number of extra inline forms."""
        self.extra = 0
        return self.extra


class PrivilegesInline(admin.TabularInline):
    model = Privileges

    def get_extra(self, request, obj=None, **kwargs):
        """Hook for customizing the number of extra inline forms."""
        self.extra = 0
        return self.extra

class UserProfilesAdmin(admin.ModelAdmin):
    # list_display = ('city', 'street', 'number', 'updated')
    # search_fields = ['city', 'street', 'number']
    # list_filter = ('city', 'street', 'created','updated',)
    inlines = [SubsidiesInline, PrivilegesInline]

# admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(PostNews)
admin.site.register(Metrics)
admin.site.register(ServicesCategory, ServiceCategoryAdmin)
admin.site.register(Services)
admin.site.register(City, CityAdmin)
admin.site.register(Street)
admin.site.register(House, HouseAdmin)
admin.site.register(Appartament)
admin.site.register(Subsidies)
admin.site.register(Privileges)
