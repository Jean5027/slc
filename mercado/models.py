from django.db import models


class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)
