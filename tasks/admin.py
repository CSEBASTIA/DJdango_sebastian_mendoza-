from django.contrib import admin
from .models import Skill, Project, Education, Certificado


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "icon")
    list_filter = ("category",)
    search_fields = ("name",)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "company", "fecha_inicio", "fecha_fin")
    search_fields = ("title", "company")
    ordering = ("-fecha_fin",)

    def save_model(self, request, obj, form, change):
        obj.full_clean()  # fuerza clean() del modelo
        super().save_model(request, obj, form, change)


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ("title", "institution", "date")
    search_fields = ("title", "institution")


@admin.register(Certificado)
class CertificadoAdmin(admin.ModelAdmin):
    list_display = ("title", "company", "date", "pdf", "enlace")
    search_fields = ("title", "company")

    def save_model(self, request, obj, form, change):
        obj.full_clean()  # fuerza clean() (PDF/enlace)
        super().save_model(request, obj, form, change)
