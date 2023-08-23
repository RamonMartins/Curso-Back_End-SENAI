from django.db import models
from apps.autores.models import *

class Categoria(models.Model):
    nome_categoria = models.CharField(max_length=200)
    def __str__(self):
        return self.nome_categoria
    

class Livro(models.Model):

    STATUS_CHOICES = (
        ("0", "PUBLISHED"),
        ("1", "DRAFT"),
        ("2", "FINISHED"),
        ("23", "EXPIRED")
    )

    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=0)

    nome_livro = models.CharField(max_length=200)
    categoria_livro = models.ManyToManyField(Categoria)
    ano_lancamento = models.CharField(max_length=4)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    autor_livro = models.ForeignKey(Autor, on_delete=models.CASCADE)
    
    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome_livro
    