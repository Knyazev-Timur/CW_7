from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin

from core.models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email')
    readonly_fields = ('last_login', 'date_joined')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Prmission', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Dates', {'fields': ('last_login', 'date_joined')}),
    )

admin.site.unregister(Group)
