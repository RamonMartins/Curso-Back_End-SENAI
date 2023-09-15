from django.db import models

class Produto(models.Model):
    foto_produto = models.ImageField(upload_to="foto_produto/")
    nome_produto = models.CharField(max_length=200)
    valor_produto = models.DecimalField(decimal_places=2, max_digits=10)
    descricao_produto = models.TextField()

    def __str__(self):
        return self.nome_produto
    