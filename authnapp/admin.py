from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from authnapp.models import User
from mainapp.models import UserProfile, Subsidies, Privileges


class UserCreationForm(forms.ModelForm):
    """Форма для создания новых пользователей. Включает все обязательные поля,
        а также повторный пароль."""
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('personal_account', 'email')

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


class PrivilegesInline(admin.TabularInline):
    model = Privileges


class UserChangeForm(forms.ModelForm):
    """Форма для обновления пользователей. Включает все поля пользователя,
    но заменяет поле пароля полем отображения хэша пароля администратора.
    """
    password = ReadOnlyPasswordHashField()


    class Meta:
        model = User
        fields = ('__all__')

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
    list_display = ('personal_account', 'name')
    # list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('personal_account', 'password')}),
        ('Personal info', {'fields': ('name','email', 'phone')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ( 'is_staff', 'personal_account', 'email', 'password1', 'password2')}
        ),
    )
    search_fields = ('personal_account', 'name')
    inlines = [UserProfileInline, SubsidiesInline, PrivilegesInline]

    ordering = ('email',)
    filter_horizontal = ()


admin.site.unregister(User)
# Now register the new UserAdmin...
admin.site.register(User, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
# admin.site.unregister(Group)




# class SubsidiesInline(admin.TabularInline):
#     model = Subsidies


# class PrivilegesInline(admin.TabularInline):
#     model = Privileges


# class UserAdmin(admin.ModelAdmin):
#     list_display = ('personal_account','name', 'is_client', 'is_staff', 'updated')
#     search_fields = ['personal_account', 'name',]
#     list_filter = ('created','updated',)
#     inlines = [UserProfileInline,]