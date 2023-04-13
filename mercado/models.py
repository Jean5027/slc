from django.db import models


class Mercado(models.Model):
    code = models.CharField(max_length=3)
    lista = models.CharField(max_length=64)

class Produtos(models.Model):
    code = models.CharField(max_length=3)
    produto = models.CharField(max_length=64)