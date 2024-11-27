from django.contrib import admin
from unfold.admin import ModelAdmin

from OpportuNest.job.models import Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'location',
        'posted_by__company__company_name',
        'date_posted',
    ]
    list_filter = [
        'location',
        'title',
        'date_posted',
    ]
    search_fields = [
        'title',
    ]
    ordering = [
        'id',
        'date_posted'
    ]