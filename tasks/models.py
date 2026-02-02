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
    orden = models.PositiveIntegerField(
        default=0
    )  # AGREGADO: para ordenar las habilidades

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["category", "orden", "name"]  # MODIFICADO: agregado orden
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
    orden = models.PositiveIntegerField(default=0)  # AGREGADO: para ordenar proyectos

    def clean(self):
        if self.fecha_inicio and self.fecha_fin and self.fecha_fin <= self.fecha_inicio:
            raise ValidationError("La fecha de fin debe ser posterior a la de inicio.")

    def __str__(self):  # AGREGADO: método __str__
        return self.title

    class Meta:
        ordering = ["orden", "-fecha_fin"]  # MODIFICADO: agregado orden
        verbose_name = "Portafolio"
        verbose_name_plural = "Portafolio"


class Education(models.Model):
    title = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    date = models.CharField(max_length=50)
    ubicacion = models.CharField(
        max_length=200, blank=True, null=True
    )  # AGREGADO: ubicación de la institución
    orden = models.PositiveIntegerField(default=0)  # AGREGADO: para ordenar educación

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["orden", "-date"]  # MODIFICADO: agregado orden
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
    orden = models.PositiveIntegerField(
        default=0
    )  # AGREGADO: para ordenar certificados

    def clean(self):
        if not self.pdf and not self.enlace:
            raise ValidationError("Debe subir un PDF o proporcionar un enlace.")
        if self.pdf and self.enlace:
            raise ValidationError("Use solo PDF o enlace, no ambos.")

    class Meta:
        ordering = ["orden", "-date"]  # MODIFICADO: agregado orden

    def __str__(self):
        return f"{self.title} - {self.company}"

    def save(self, *args, **kwargs):
        self.full_clean()  # valida antes de guardar
        super().save(*args, **kwargs)


class Experience(models.Model):
    puesto = models.CharField(max_length=120)
    empresa = models.CharField(max_length=120)
    fecha_inicio = models.CharField(max_length=30)  # simple (ej: "2023")
    fecha_fin = models.CharField(max_length=30, blank=True, null=True)  # "Presente"
    descripcion = models.TextField(blank=True)
    orden = models.PositiveIntegerField(default=0)  # para controlar el orden
    activo = models.BooleanField(default=True)

    class Meta:
        ordering = ["orden", "-id"]
        verbose_name = "Experiencia Laboral"  # AGREGADO: nombre singular
        verbose_name_plural = "Experiencia Laboral"  # AGREGADO: nombre plural

    def __str__(self):
        return f"{self.puesto} - {self.empresa}"


# Al final de tu models.py, agrega:


class Idioma(models.Model):
    NIVEL_CHOICES = [
        ("nativo", "Nativo"),
        ("c2", "C2 - Dominio"),
        ("c1", "C1 - Avanzado"),
        ("b2", "B2 - Intermedio Alto"),
        ("b1", "B1 - Intermedio"),
        ("a2", "A2 - Básico"),
        ("a1", "A1 - Principiante"),
    ]

    nombre = models.CharField(max_length=50)
    nivel = models.CharField(max_length=20, choices=NIVEL_CHOICES)
    descripcion_nivel = models.CharField(
        max_length=100, blank=True, null=True
    )  # ej: "B1 Intermedio"
    orden = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["orden", "nombre"]
        verbose_name = "Idioma"
        verbose_name_plural = "Idiomas"

    def __str__(self):
        return f"{self.nombre} - {self.get_nivel_display()}"
