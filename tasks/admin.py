from django.contrib import admin
from .models import Skill, Project, Education

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'icon')
    list_filter = ('category',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'date')
    search_fields = ('title', 'company')

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('title', 'institution', 'date')
    search_fields = ('title', 'institution')