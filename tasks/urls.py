from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("certificados/", views.certificados, name="certificados"),
    path("download-cv/", views.download_cv, name="download_cv"),
    path("portafolio/", views.portafolio, name="portafolio"),
    path("productos/", views.productos, name="productos"),
]
