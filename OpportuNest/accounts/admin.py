from django.contrib import admin
from unfold.admin import ModelAdmin

from OpportuNest.accounts.forms import SeekerCreationForm, SeekerEditForm, CompanyCreationForm, CompanyEditForm
from OpportuNest.accounts.models import AppUser, Seeker, Company


@admin.register(AppUser)
class AppUserAdmin(ModelAdmin):
    list_display = [
        'id',
        'email',
        'is_staff',
        'is_superuser',
    ]
    ordering = [
        'id',
    ]
    list_filter = [
        'is_staff'
    ]
    search_fields = [
        'email'
    ]


@admin.register(Seeker)
class SeekerAdmin(ModelAdmin):
    model = Seeker
    add_form = SeekerCreationForm
    form = SeekerEditForm

    list_display = [
        'id',
        'first_name',
        'last_name',
    ]

    ordering = [
        'id'
    ]
    search_fields = [
        'first_name',
        'last_name'
    ]


@admin.register(Company)
class CompanyAdmin(ModelAdmin):
    model = Company
    add_form = CompanyCreationForm
    form = CompanyEditForm

    list_display = [
        'id',
        'company_name',
    ]

    ordering = [
        'id'
    ]
    search_fields = [
        'company_name'
    ]