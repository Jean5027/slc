from django.db import models


class Mercado(models.Model):
    code = models.CharField(max_length=3)
    lista = models.CharField(max_length=64)

class Produtos(models.Model):
    code = models.CharField(max_length=3)
    produto = models.CharField(max_length=64)

class Usuario (models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    produtos = models.ManyToManyField(Produtos, blank=True, related_name="usuarios")

    def __str__(self):
        return f"{self.first} {self.last}"