from typing import Iterable, Optional
from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=200, null=True, blank=True)
    idade = models.IntegerField(null=True, blank=True)
    data_nascimento = models.DateTimeField()
    email = models.EmailField()
    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
