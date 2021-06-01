from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.models import Group

from authnapp.models import User
from mainapp.models import CurrentCounter, HistoryCounter, Privileges, Recalculations, Subsidies, UserProfile


class UserCreationForm(forms.ModelForm):
    """Форма для создания новых пользователей. Включает все обязательные поля,
    а также повторный пароль."""

    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Подтверждение пароля", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("personal_account", "email")

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Пароли не совпадают")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserProfileInline(admin.TabularInline):
    model = UserProfile


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


class UserChangeForm(forms.ModelForm):
    """Форма для обновления пользователей. Включает все поля пользователя,
    но заменяет поле пароля полем отображения хэша пароля администратора.
    """

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = "__all__"

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ("personal_account", "name")
    # list_filter = ('is_admin',)
    fieldsets = (
        (None, {"fields": ("personal_account", "password")}),
        ("Персональные данные", {"fields": ("name", "email", "phone")}),
        ("Разрешения", {"fields": ("is_active", "is_staff", "is_superuser", "groups")}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {"classes": ("wide",), "fields": ("is_staff", "personal_account", "email", "password1", "password2")}),
    )
    search_fields = ("personal_account", "name")
    # inlines = [UserProfileInline, SubsidiesInline, PrivilegesInline, RecalculationsInline, CurrentCounterInline, HistoryCounterInline]

    ordering = ("email",)
    filter_horizontal = ()

    # Тестово, доработать
    # https://coderoad.ru/10356491/%D0%A1%D0%BA%D1%80%D1%8B%D1%82%D1%8C-%D0%BE%D0%BF%D1%80%D0%B5%D0%B4%D0%B5%D0%BB%D0%B5%D0%BD%D0%BD%D1%8B%D0%B5-%D0%BF%D0%BE%D0%BB%D1%8F-%D0%B2-Django-admin-%D1%81%D0%B0%D0%B9%D1%82%D0%B5-%D0%B4%D0%BB%D1%8F-%D1%80%D0%B0%D0%B7%D0%BD%D1%8B%D1%85-%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D0%B5%D0%B9
    def get_type_counter(self, obj):
        if self.username == "admin":
            return "CC"
        return "XXX"


admin.site.unregister(User)
# Now register the new UserAdmin...
admin.site.register(User, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
# admin.site.unregister(Group)
