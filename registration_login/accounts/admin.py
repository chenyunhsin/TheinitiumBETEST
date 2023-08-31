from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    fieldsets = UserAdmin.fieldsets + (('Custom fields', {'fields': ('is_employee',)}),)

admin.site.register(CustomUser, CustomUserAdmin)
