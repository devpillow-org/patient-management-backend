# Register your models here.

from django.contrib import admin

from account.domain.models import EmployeProfile, Function, User


@admin.register(User, EmployeProfile, Function)
class UserAdmin(admin.ModelAdmin):  # type: ignore
    pass
