from django.contrib import admin
from .models import Skill, Project, Education, Certificado, Experience, Idioma


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ["puesto", "empresa", "fecha_inicio", "fecha_fin", "activo", "orden"]
    list_editable = ["orden", "activo"]
    list_filter = ["activo"]
    search_fields = ["puesto", "empresa"]
    ordering = ["orden", "-id"]


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ["name", "category", "icon", "orden"]
    list_filter = ["category"]
    list_editable = ["orden"]
    search_fields = ["name"]
    ordering = ["category", "orden", "name"]


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ["title", "institution", "date", "orden"]
    list_editable = ["orden"]
    search_fields = ["title", "institution"]
    ordering = ["orden", "-date"]


@admin.register(Certificado)
class CertificadoAdmin(admin.ModelAdmin):
    list_display = ["title", "company", "date", "tiene_pdf", "tiene_enlace", "orden"]
    list_editable = ["orden"]
    search_fields = ["title", "company"]
    ordering = ["orden", "-date"]

    def tiene_pdf(self, obj):
        return "✓" if obj.pdf else "✗"

    tiene_pdf.short_description = "PDF"

    def tiene_enlace(self, obj):
        return "✓" if obj.enlace else "✗"

    tiene_enlace.short_description = "Enlace"

    def save_model(self, request, obj, form, change):
        obj.full_clean()
        super().save_model(request, obj, form, change)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["title", "company", "fecha_inicio", "fecha_fin", "orden"]
    list_editable = ["orden"]
    search_fields = ["title", "company"]
    ordering = ["orden", "-fecha_fin"]

    def save_model(self, request, obj, form, change):
        obj.full_clean()
        super().save_model(request, obj, form, change)


@admin.register(Idioma)
class IdiomaAdmin(admin.ModelAdmin):
    list_display = ["nombre", "nivel", "descripcion_nivel", "orden"]
    list_editable = ["orden"]
    list_filter = ["nivel"]
    search_fields = ["nombre"]
    ordering = ["orden", "nombre"]
