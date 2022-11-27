from django.db import models

class Pessoas(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=20)

