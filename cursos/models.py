from django.db import models

# Create your models here.
class Cursos(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False, default='Curso')
    description = models.TextField(null=False, blank=False)
    level = models.CharField(max_length=50, null=False, blank=False,default="Iniciante")
    duration = models.CharField(max_length=50, null=False, blank=False)
    image = models.ImageField(upload_to='courses_images/', blank=True, null=True)
    format = models.CharField(max_length=50, null=False, blank=False, default='Online')
    modules = models.TextField(blank=True, null=True)
    price = models.FloatField(null=False, blank=False, default=0)
    vacancies = models.IntegerField(null=False, blank=False)
    begin = models.DateField(null=True, blank=True)
    end = models.DateField(null=True, blank=True)
    createdAt = models.DateField(auto_created=True)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.title