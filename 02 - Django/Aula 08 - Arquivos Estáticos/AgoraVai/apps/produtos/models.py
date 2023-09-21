from django.db import models

class Produto(models.Model):
    nome_produto = models.CharField(max_length=200)
    descricao_produto = models.TextField()
    valor_produto = models.DecimalField(max_digits=10, decimal_places=2)
    foto_produto = models.ImageField(upload_to='foto_produto/')

    def __str__(self):
        return self.nome_produto