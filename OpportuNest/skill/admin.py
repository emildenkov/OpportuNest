from django.contrib import admin
from unfold.admin import ModelAdmin

from OpportuNest.skill.models import Skill


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    pass