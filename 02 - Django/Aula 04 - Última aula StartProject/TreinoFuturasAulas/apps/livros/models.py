from django.db import models

class Livro(models.Model):
    nome_livro = models.CharField(max_length=200)
    autor_livro = models.ForeignKey("autores.Autor", on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_livro
    
class Genero(models.Model):
    nome_genero = models.CharField(max_length=200)

    def __str__(self):
        return self.nome_genero
    