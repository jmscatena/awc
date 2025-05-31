from django.db import models

# Create your models here.
class Areas(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.TextField()
    def __str__(self):
        return self.titulo

class Inovacoes(models.Model):
    titulo = models.CharField(max_length=50,null=False,blank=False)
    descricao = models.TextField(null=False, blank=False)
    empresa = models.CharField(max_length=50, null=True, blank=True)
    repositorio = models.CharField(max_length=100, null=True, blank=True)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    criado_em = models.DateTimeField(auto_now_add=True)
    areas = models.ManyToManyField(Areas)
    def __str__(self):
        return self.titulo
