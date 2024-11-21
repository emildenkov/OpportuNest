from django.contrib import admin
from unfold.admin import ModelAdmin

from OpportuNest.application.models import Application


@admin.register(Application)
class ApplicationAdmin(ModelAdmin):
    pass

