from django.db import models

class Produto(models.Model):
    nome_produto = models.CharField(max_length=200)
    valor_produto = models.DecimalField(max_digits=1000, decimal_places=2)

    def __str__(self):
        return self.nome_produto
    
