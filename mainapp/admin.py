from django.contrib import admin
from django.db.models.base import ModelState
from authnapp.models import User


from mainapp.models import ServicesCategory, Services, Metrics, City, Street, UK, House 
from mainapp.models import HouseCurrent, HouseHistory, Appartament, UserProfile, CurrentCounter, HistoryCounter
from mainapp.models import ConstantPayments, VariablePayments, Subsidies, Privileges, Profit, Payment, Recalculations, Standart

class CommentInline(admin.TabularInline):
    model = Services


class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'updated')
    search_fields = ['name',]
    list_filter = ('created','updated',)
    inlines = [CommentInline,]


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'updated')
    search_fields = ['name',]
    list_filter = ('category', 'created','updated',)
    # inlines = [CommentInline,]


class CityAdmin(admin.ModelAdmin):
    list_display = ('city','updated')
    search_fields = ['city',]
    list_filter = ('created','updated',)



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
# admin.site.register(Appartament, UserProfile, CurrentCounter, HistoryCounter, ConstantPayments, VariablePayments)
# admin.site.register(Subsidies, Privileges, Profit, Payment, Recalculations, Standart)
