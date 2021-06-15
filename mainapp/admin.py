from django.contrib import admin
from django.db import models
from django.db.models.base import ModelState
from authnapp.models import User

from authnapp.models import User
from mainapp.models import (
    UK,
    Appartament,
    City,
    ConstantPayments,
    CurrentCounter,
    HistoryCounter,
    House,
    HouseCurrent,
    HouseHistory,
    Metrics,
    Payment,
    Privileges,
    Profit,
    Recalculations,
    Services,
    ServicesCategory,
    Standart,
    Street,
    Subsidies,
    UserProfile,
    VariablePayments,
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
    inlines = [
        ServicesInline,
    ]


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
        self.extra = 0
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


class AppartamentInline(admin.TabularInline):
    model = Appartament

    def get_extra(self, request, obj=None, **kwargs):
        """Hook for customizing the number of extra inline forms."""
        self.extra = 0
        return self.extra


class HouseCurrentInline(admin.TabularInline):
    model = HouseCurrent

    def get_extra(self, request, obj=None, **kwargs):
        """Hook for customizing the number of extra inline forms."""
        self.extra = 0
        return self.extra


class HouseHistoryInline(admin.TabularInline):
    model = HouseHistory

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
    inlines = [HouseCurrentInline, AppartamentInline, HouseHistoryInline]


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


class CurrentCounterInline(admin.TabularInline):
    model = CurrentCounter

    def get_extra(self, request, obj=None, **kwargs):
        """Hook for customizing the number of extra inline forms."""
        self.extra = 0
        return self.extra


class HistoryCounterInline(admin.TabularInline):
    model = HistoryCounter

    def get_extra(self, request, obj=None, **kwargs):
        """Hook for customizing the number of extra inline forms."""
        self.extra = 0
        return self.extra


class RecalculationsInline(admin.TabularInline):
    model = Recalculations

    def get_extra(self, request, obj=None, **kwargs):
        """Hook for customizing the number of extra inline forms."""
        self.extra = 0
        return self.extra


class UserProfilesAdmin(admin.ModelAdmin):
    # list_display = ('city', 'street', 'number', 'updated')
    # search_fields = ['city', 'street', 'number']
    # list_filter = ('city', 'street', 'created','updated',)
    inlines = [SubsidiesInline, PrivilegesInline, RecalculationsInline, CurrentCounterInline, HistoryCounterInline]


admin.site.register(ServicesCategory)
admin.site.register(Services)
admin.site.register(City)
admin.site.register(Metrics)
admin.site.register(Street)
admin.site.register(UK)
admin.site.register(House)
admin.site.register(HouseCurrent)
admin.site.register(HouseHistory)
admin.site.register(User)
admin.site.register(Appartament)
admin.site.register(UserProfile)
admin.site.register(CurrentCounter)
admin.site.register(HistoryCounter)
admin.site.register(ConstantPayments)
admin.site.register(VariablePayments)
admin.site.register(Subsidies)
admin.site.register(Privileges)
admin.site.register(Profit)
admin.site.register(Payment)
admin.site.register(Recalculations)
admin.site.register(Standart)
