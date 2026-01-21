from django.db import models

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


class Project(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    date = models.CharField(max_length=50)
    description = models.TextField()
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-date']


class Education(models.Model):
    title = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    date = models.CharField(max_length=50)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-date']