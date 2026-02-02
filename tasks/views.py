from django.shortcuts import render
from django.views.decorators.http import require_POST

from .models import Certificado, Project, Education, Skill, Experience, Idioma


def home(request):
    context = {
        # CV
        "experiencias": Experience.objects.filter(activo=True).order_by("orden", "-id"),
        "educaciones": Education.objects.all().order_by("orden"),
        "idiomas": Idioma.objects.all().order_by("orden", "nombre"),
        # Skills por categoría (tu modelo usa category: backend/frontend/tools)
        "habilidades_backend": Skill.objects.filter(category="backend").order_by(
            "orden", "name"
        ),
        "habilidades_frontend": Skill.objects.filter(category="frontend").order_by(
            "orden", "name"
        ),
        "herramientas": Skill.objects.filter(category="tools").order_by(
            "orden", "name"
        ),
        # Portafolio
        "projects": Project.objects.all().order_by("orden", "-fecha_fin"),
    }
    return render(request, "home.html", context)


def certificados(request):
    certificados = Certificado.objects.all().order_by("orden", "-date")
    return render(request, "certificados.html", {"certificados": certificados})


def portafolio(request):
    projects = Project.objects.all().order_by("orden", "-fecha_fin")
    return render(request, "portafolio.html", {"projects": projects})


def productos(request):
    return render(request, "productos.html")


@require_POST
def download_cv(request):
    incluir_general = request.POST.get("general") == "on"
    incluir_formacion = request.POST.get("formacion") == "on"
    incluir_certificados = request.POST.get("certificados") == "on"
    incluir_portafolio = request.POST.get("portafolio") == "on"

    context = {
        "incluir_general": incluir_general,
        "incluir_formacion": incluir_formacion,
        "incluir_certificados": incluir_certificados,
        "incluir_portafolio": incluir_portafolio,
        "experiencias": Experience.objects.filter(activo=True).order_by("orden", "-id"),
        "educaciones": Education.objects.all().order_by("orden"),
        "certificados": Certificado.objects.all().order_by("orden", "-date"),
        "proyectos": Project.objects.all().order_by("orden", "-fecha_fin"),
        "habilidades_backend": Skill.objects.filter(category="backend").order_by(
            "orden", "name"
        ),
        "habilidades_frontend": Skill.objects.filter(category="frontend").order_by(
            "orden", "name"
        ),
        "herramientas": Skill.objects.filter(category="tools").order_by(
            "orden", "name"
        ),
        "idiomas": Idioma.objects.all().order_by("orden", "nombre"),
    }

    return render(request, "cv_pdf.html", context)
