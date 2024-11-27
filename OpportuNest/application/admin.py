from django.contrib import admin
from unfold.admin import ModelAdmin

from OpportuNest.application.models import Application


@admin.register(Application)
class ApplicationAdmin(ModelAdmin):
    list_display = [
        'id',
        'job__posted_by__company__company_name',
        'applicant__seeker__first_name',
        'status',
        'date_applied'
    ]
    list_filter = [
        'status',
        'date_applied'
    ]
    ordering = [
        'id',
        'date_applied'
    ]
    search_fields = [
        'job__posted_by__company__company_name',
        'applicant__seeker__first_name'
    ]

