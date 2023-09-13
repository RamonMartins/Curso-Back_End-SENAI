from django.db import models

class Livro(models.Model):
    titulo_livro = models.CharField(max_length=200)
    descricao_livro = models.TextField()
    lido_status = models.BooleanField(default=False)
    autor_livro = models.ForeignKey("autores.Autor", on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo_livro
