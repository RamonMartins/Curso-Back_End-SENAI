from django.db import models

class Autor(models.Model):
    nome_autor = models.CharField(max_length=200)
    idade_autor = models.PositiveIntegerField()

    def __str__(self):
        return self.nome_autor
