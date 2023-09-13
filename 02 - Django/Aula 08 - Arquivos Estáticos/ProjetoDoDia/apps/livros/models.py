from django.db import models

class Livro(models.Model):
    titulo_livro = models.CharField(max_length=200)
    descricao_livro = models.TextField()

    def __str__(self):
        return self.titulo_livro
    