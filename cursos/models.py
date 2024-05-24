from django.db import models

# Create your models here.
class Cursos(models.Model):
    titulo = models.CharField(max_length=50, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    vagas = models.IntegerField(null=False, blank=False)
    data_inicio = models.DateField(null=True, blank=True)
    data_fim = models.DateField(null=True, blank=True)
    creado_em = models.DateField(auto_created=True)
    ativo = models.BooleanField(default=True)
    def __str__(self):
        return self.titulo