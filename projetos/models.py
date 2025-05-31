from django.db import models
from django.db import models


# Create your models here.
class Projetos(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    client = models.CharField(max_length=100)
    image = models.ImageField(upload_to='projects_images/', blank=True, null=True)
    highlights = models.TextField(blank=True,null=True)
    duration = models.IntegerField(default=0)
    year = models.IntegerField(default=2025)
    repository = models.CharField(max_length=100, blank=True, null=True)
    begin = models.DateField()
    end = models.DateField()
    value = models.FloatField()
    createdAt = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.title
