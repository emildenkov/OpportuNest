from django.contrib import admin
from unfold.admin import ModelAdmin

from OpportuNest.accounts.models import AppUser


@admin.register(AppUser)
class AppUserAdmin(ModelAdmin):
    pass
