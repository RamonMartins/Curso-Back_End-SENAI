from django.db import models

class Criador(models.Model):
    nome_criador = models.CharField(max_length=200)
    idade_criador = models.PositiveIntegerField()

    def __str__(self):
        return self.nome_criador
    
