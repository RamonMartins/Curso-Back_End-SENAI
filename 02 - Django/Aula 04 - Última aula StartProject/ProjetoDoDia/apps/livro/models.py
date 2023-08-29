from django.db import models

class Livro(models.Model):
    nome_livro = models.CharField(max_length=200)
    autor_livro = models.ForeignKey("autor.Autor", on_delete=models.CASCADE)
    teste = models.IntegerField(null=True, blank=True)
    oi = models.ManyToManyField

    def __str__(self):
        return self.nome_livro
    