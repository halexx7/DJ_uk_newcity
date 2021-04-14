from django.contrib import admin
from django.db import models
from django.db.models.base import ModelState
from authnapp.models import User


from mainapp.models import ServicesCategory, Services, Metrics, City, Street, UK, House 
from mainapp.models import HouseCurrent, HouseHistory, Appartament, UserProfile, CurrentCounter, HistoryCounter
from mainapp.models import ConstantPayments, VariablePayments, Subsidies, Privileges, Profit, Payment, Recalculations, Standart

class ServicesInline(admin.TabularInline):
    model = Services


class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'updated')
    search_fields = ['name',]
    list_filter = ('created','updated',)
    inlines = [ServicesInline,]


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'updated')
    search_fields = ['name',]
    list_filter = ('category', 'created','updated',)
    # inlines = [CommentInline,]


class CityAdmin(admin.ModelAdmin):
    list_display = ('city','updated')
    search_fields = ['city',]
    list_filter = ('created','updated',)


class UserProfileInline(admin.TabularInline):
    model = UserProfile


class SubsidiesInline(admin.TabularInline):
    model = Subsidies


class PrivilegesInline(admin.TabularInline):
    model = Privileges


class UserAdmin(admin.ModelAdmin):
    list_display = ('personal_account','name', 'is_client', 'is_staff', 'updated')
    search_fields = ['personal_account', 'name',]
    list_filter = ('created','updated',)
    inlines = [UserProfileInline,]


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('name','updated')
    search_fields = ['name',]
    list_filter = ('created','updated',)
    inlines = [SubsidiesInline,]


admin.site.register(ServicesCategory, ServiceCategoryAdmin)
admin.site.register(Services, ServiceAdmin)
admin.site.register(City, CityAdmin)
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
