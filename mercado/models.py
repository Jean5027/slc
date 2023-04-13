from django.db import models


class Mercado(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)
