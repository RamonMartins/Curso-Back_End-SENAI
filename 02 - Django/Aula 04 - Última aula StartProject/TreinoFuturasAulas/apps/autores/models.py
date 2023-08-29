from django.db import models

class Autor(models.Model):
    nome_autor = models.CharField(max_length=200)
    idade_autor = models.IntegerField()
    foto_autor = models.ImageField(upload_to="foto_perfil/")
    genero_autor = models.ForeignKey("livros.Genero", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nome_autor
    



