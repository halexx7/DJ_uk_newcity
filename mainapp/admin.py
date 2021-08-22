from django.contrib import admin

from authnapp.models import User
from mainapp.models import (
    AverageСalculationBuffer,
    ConstantPayments,
    CurrentCounter,
    HeaderData,
    HistoryCounter,
    HouseCurrent,
    HouseHistory,
    MainBook,
    PaymentOrder,
    PersonalAccountStatus,
    Recalculations,
    Standart,
    VariablePayments,
)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(HouseCurrent)
class HouseCurrentAdmin(admin.ModelAdmin):
    list_display = ("house", "period", "col_water", "hot_water")
    search_fields = ["house", "period"]
    list_filter = (
        "house",
        "created",
        "updated",
    )


@admin.register(HouseHistory)
class HouseHistoryAdmin(admin.ModelAdmin):
    list_display = ("house", "period", "col_water", "hot_water")
    search_fields = ["house", "period"]
    list_filter = (
        "house",
        "created",
        "updated",
    )


@admin.register(Standart)
class StandartAdmin(admin.ModelAdmin):
    list_display = ("house", "period", "col_water", "hot_water")
    search_fields = ["house", "period"]
    list_filter = (
        "house",
        "created",
        "updated",
    )


@admin.register(CurrentCounter)
class CurrentCounterAdmin(admin.ModelAdmin):
    list_display = ("user", "period", "col_water", "hot_water")
    search_fields = ["user", "period"]
    list_filter = (
        "user",
        "created",
        "updated",
    )


@admin.register(HistoryCounter)
class HistoryCounterAdmin(admin.ModelAdmin):
    list_display = ("user", "period", "col_water", "hot_water")
    search_fields = ["user", "period"]
    list_filter = (
        "user",
        "created",
        "updated",
    )


@admin.register(Recalculations)
class RecalculationsAdmin(admin.ModelAdmin):
    list_display = ("user", "period", "service", "desc")
    search_fields = ["user", "period", "service"]
    list_filter = (
        "user",
        "created",
        "updated",
    )


@admin.register(ConstantPayments)
class ConstantPaymentsAdmin(admin.ModelAdmin):
    list_display = ("user", "pre_total")
    search_fields = [
        "user",
    ]
    list_filter = (
        "user",
        "created",
        "updated",
    )


@admin.register(VariablePayments)
class VariablePaymentsAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "period",
        "pre_total",
    )
    search_fields = [
        "user",
        "period",
    ]
    list_filter = (
        "user",
        "created",
        "updated",
    )


@admin.register(HeaderData)
class HeaderDataAdmin(admin.ModelAdmin):
    list_display = ("user", "updated")
    search_fields = [
        "user",
        "period",
    ]
    list_filter = (
        "user",
        "created",
        "updated",
    )


@admin.register(MainBook)
class MainBookAdmin(admin.ModelAdmin):
    list_display = ("user", "period", "direction", "amount")
    search_fields = [
        "user",
        "period",
    ]
    list_filter = (
        "user",
        "period",
        "direction",
        "updated",
    )


@admin.register(PaymentOrder)
class PaymentOrderAdmin(admin.ModelAdmin):
    list_display = ("user", "period", "pre_amount")
    search_fields = [
        "user",
        "period",
    ]
    list_filter = (
        "user",
        "period",
        "created",
        "updated",
    )


@admin.register(PersonalAccountStatus)
class PersonalAccountStatusAdmin(admin.ModelAdmin):
    list_display = ("user", "amount")
    search_fields = [
        "user",
    ]
    list_filter = (
        "user",
        "created",
        "updated",
    )


@admin.register(AverageСalculationBuffer)
class AverageСalculationBufferAdmin(admin.ModelAdmin):
    list_display = ("user", "col_water", "hot_water")
    search_fields = [
        "user",
    ]
    list_filter = (
        "user",
        "created",
        "updated",
    )
