from django.db import models
from django.db.models import Model

class Empresa(models.Model):
    nome = models.CharField(max_length=150)
    cnpj = models.CharField(max_length=14)
    email = models.EmailField(max_length=50)


class Produto(models.Model):
    nome = models.CharField(max_length=150)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=5)
    descricao = models.CharField(max_length=150)
    marca = models.CharField(max_length=50)
    valor = models.CharField(max_length=10)
