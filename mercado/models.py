from django.db import models

class Lista(models.Model):
    nome = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return f"{self.id}: {self.nome}"


class Produtos(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.FloatField()
    lista = models.ManyToManyField(Lista, blank=True, related_name="produtos")

    def __str__(self) -> str:
        return f"{self.id}: {self.nome} | R${self.preco: .2f}"
        

class Usuario (models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    produtos = models.ManyToManyField(Produtos, blank=True, related_name="usuarios")

    def __str__(self):
        return f"{self.first} {self.last}"