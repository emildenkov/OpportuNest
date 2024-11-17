from django.contrib import admin
from unfold.admin import ModelAdmin

from OpportuNest.accounts.models import AppUser, Seeker, Company


@admin.register(AppUser)
class AppUserAdmin(ModelAdmin):
    pass


@admin.register(Seeker)
class Admin(ModelAdmin):
    pass


@admin.register(Company)
class CompanyAdmin(ModelAdmin):
    pass