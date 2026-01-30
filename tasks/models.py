from django.db import models
from django.core.validators import FileExtensionValidator


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('backend', 'Backend'),
        ('frontend', 'Frontend'),
        ('tools', 'Herramientas'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    icon = models.CharField(max_length=10, default='⚙️')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['category', 'name']
        verbose_name = "Información General"
        verbose_name_plural = "Información General"


class Project(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    date = models.CharField(max_length=50)
    description = models.TextField()
    pdf = models.FileField(
        upload_to='portafolios/',
        validators=[FileExtensionValidator(allowed_extensions=['pdf'])],
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date']
        verbose_name = "Portafolio"
        verbose_name_plural = "Portafolio"


class Education(models.Model):
    title = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    date = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date']
        verbose_name = "Formación académica"
        verbose_name_plural = "Formación académica"


class Certificado(models.Model):
    nombre = models.CharField(max_length=200)
    plataforma = models.CharField(max_length=200, blank=True)
    enlace = models.URLField()
    fecha_obtencion = models.DateField(blank=True, null=True)
    
    class Meta:
        ordering = ['-fecha_obtencion']
        verbose_name = "Certificados"
        verbose_name_plural = "Certificados"
    
    def __str__(self):
        return self.nombre