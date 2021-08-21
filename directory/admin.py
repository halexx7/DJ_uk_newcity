from django.contrib import admin

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


@admin.register(ServicesCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "updated", "is_active")
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


@admin.register(Services)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "updated", "is_active")
    search_fields = ["name", "category", "unit"]
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


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ("city", "updated", "is_active")
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


@admin.register(Street)
class StreetAdmin(admin.ModelAdmin):
    list_display = ("street", "city", "updated", "is_active")
    search_fields = ["city", "street"]
    list_filter = (
        "created",
        "updated",
    )
    inlines = [
        HouseInline,
    ]


class AppartamentInline(admin.TabularInline):
    model = Appartament

    def get_extra(self, request, obj=None, **kwargs):
        """Hook for customizing the number of extra inline forms."""
        self.extra = 0
        return self.extra


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ("street", "number", "updated", "is_active")
    search_fields = ["street", "number"]
    list_filter = (
        "created",
        "updated",
    )
    inlines = [
        AppartamentInline,
    ]


@admin.register(PostNews)
class PostNewsAdmin(admin.ModelAdmin):
    list_display = ("title", "created", "is_active")
    search_fields = [
        "title",
    ]
    list_filter = (
        "created",
        "updated",
    )


@admin.register(UserProfile)
class PostNewsAdmin(admin.ModelAdmin):
    list_display = ("user", "created", "is_active")
    search_fields = [
        "user",
    ]
    list_filter = ("created", "updated", "gender")


@admin.register(Metrics)
class MetricsAdmin(admin.ModelAdmin):
    list_display = ("name", "created", "is_active")
    search_fields = [
        "name",
    ]
    list_filter = (
        "created",
        "updated",
    )


@admin.register(Appartament)
class AppartamentAdmin(admin.ModelAdmin):
    list_display = ("house", "number", "is_active")
    search_fields = ["house", "user"]
    list_filter = (
        "house",
        "created",
        "updated",
    )


@admin.register(Subsidies)
class SubsidiesAdmin(admin.ModelAdmin):
    list_display = ("user", "service", "sale", "is_active")
    search_fields = ["service", "user"]
    list_filter = (
        "user",
        "service",
        "created",
        "updated",
    )


@admin.register(Privileges)
class PrivilegesAdmin(admin.ModelAdmin):
    list_display = ("user", "service", "sale", "is_active")
    search_fields = ["service", "user"]
    list_filter = (
        "user",
        "service",
        "created",
        "updated",
    )
