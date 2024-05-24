from django.db import models

# Create your models here.
class Projetos(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    empresa = models.CharField(max_length=100)
    repositorio = models.CharField(max_length=100)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    valor = models.FloatField()
    criado_em = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)
    def __str__(self):
        return self.titulo