from django.db import models
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ("backend", "Backend"),
        ("frontend", "Frontend"),
        ("tools", "Herramientas"),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    icon = models.CharField(max_length=10, default="⚙️")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["category", "name"]
        verbose_name = "Información General"
        verbose_name_plural = "Información General"


class Project(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)

    # defaults temporales
    fecha_inicio = models.DateField(default="2023-12-31")
    fecha_fin = models.DateField(default="2024-01-01")

    description = models.TextField()
    url_demo = models.URLField(blank=True, null=True)
    url_repo = models.URLField(blank=True, null=True)

    def clean(self):
        if self.fecha_inicio and self.fecha_fin and self.fecha_fin <= self.fecha_inicio:
            raise ValidationError("La fecha de fin debe ser posterior a la de inicio.")

    class Meta:
        ordering = ["-fecha_fin"]
        verbose_name = "Portafolio"
        verbose_name_plural = "Portafolio"


class Education(models.Model):
    title = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    date = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-date"]
        verbose_name = "Formación académica"
        verbose_name_plural = "Formación académica"


class Certificado(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    date = models.CharField(max_length=50)
    description = models.TextField()

    pdf = models.FileField(
        upload_to="certificados/",
        validators=[FileExtensionValidator(["pdf"])],
        blank=True,
        null=True,
    )
    enlace = models.URLField(blank=True, null=True)

    def clean(self):
        if not self.pdf and not self.enlace:
            raise ValidationError("Debe subir un PDF o proporcionar un enlace.")
        if self.pdf and self.enlace:
            raise ValidationError("Use solo PDF o enlace, no ambos.")

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return f"{self.title} - {self.company}"

    def save(self, *args, **kwargs):
        self.full_clean()  # valida antes de guardar
        super().save(*args, **kwargs)
