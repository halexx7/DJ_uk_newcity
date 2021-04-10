from django.contrib import admin
from django.db.models.base import ModelState

import mainapp.models


admin.site.register(mainapp.models.ServicesCategory)
admin.site.register(mainapp.models.Services)
admin.site.register(mainapp.models.City)
admin.site.register(mainapp.models.Street)
admin.site.register(mainapp.models.UK)
admin.site.register(mainapp.models.House)
admin.site.register(mainapp.models.HouseCurrent)
admin.site.register(mainapp.models.HouseHistory)
admin.site.register(mainapp.models.Appartament)
admin.site.register(mainapp.models.User)
admin.site.register(mainapp.models.UserProfile)
admin.site.register(mainapp.models.CurrentCounter)
admin.site.register(mainapp.models.HistoryCounter)
admin.site.register(mainapp.models.ConstantPayments)
admin.site.register(mainapp.models.VariablePayments)
admin.site.register(mainapp.models.Subsidies)
admin.site.register(mainapp.models.Privileges)
admin.site.register(mainapp.models.Profit)
admin.site.register(mainapp.models.Payment)
admin.site.register(mainapp.models.Recalculations)