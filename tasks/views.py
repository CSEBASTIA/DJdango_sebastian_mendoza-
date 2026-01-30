from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from .models import Certificado, Project, Education, Skill

def home(request):
    projects = Project.objects.all()
    return render(request, "home.html", {'projects': projects})

def certificados(request):
    certificados = Certificado.objects.all()
    return render(request, "certificados.html", {'certificados': certificados})

def portafolio(request):
    projects = Project.objects.all()
    return render(request, "portafolio.html", {'projects': projects})

@require_POST
def download_cv(request):
    incluir_general = request.POST.get('general') == 'on'
    incluir_formacion = request.POST.get('formacion') == 'on'
    incluir_certificados = request.POST.get('certificados') == 'on'
    incluir_portafolio = request.POST.get('portafolio') == 'on'

    # Si selecciona Información General, descarga el PDF directamente
    if incluir_general:
        try:
            with open('static/cv/Carlos Sebastian_Mendoza Avellan_CV.pdf', 'rb') as pdf:
                response = HttpResponse(pdf.read(), content_type='application/pdf')
                response['Content-Disposition'] = 'attachment; filename="Carlos Sebastian_Mendoza Avellan_CV.pdf"'
                return response
        except FileNotFoundError:
            pass  # Si no existe, continúa con la plantilla

    context = {
        'incluir_general': incluir_general,
        'incluir_formacion': incluir_formacion,
        'incluir_certificados': incluir_certificados,
        'incluir_portafolio': incluir_portafolio,
        'educaciones': Education.objects.all(),
        'certificados': Certificado.objects.all(),
        'proyectos': Project.objects.all(),
        'skills': Skill.objects.all(),
    }
    
    return render(request, 'cv_pdf.html', context)
def productos(request):
    return render(request, "productos.html")