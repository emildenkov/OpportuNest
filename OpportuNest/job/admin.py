from django.contrib import admin
from unfold.admin import ModelAdmin

from OpportuNest.job.models import Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    pass