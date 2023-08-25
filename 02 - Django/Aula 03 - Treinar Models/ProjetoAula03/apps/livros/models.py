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
        ("3", "EXPIRED")
    )

    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=0, null=True, blank=True)

    nome_livro = models.CharField(max_length=200)
    categoria_livro = models.OneToOneField(Categoria, on_delete=models.CASCADE, null=True, blank=True)
    ano_lancamento = models.CharField(max_length=4)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    autor_livro = models.ForeignKey(Autor, on_delete=models.CASCADE)
    
    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome_livro
    
    #def save(self, *args, **kwargs):
    #    if self.categoria_livro == None:
    #        self.nome_livro = "mudou2"
    #
    #    super().save(*args, **kwargs)

    class Meta:
        ordering = ('pk',)
        verbose_name = 'Livro do Ramon'
        verbose_name_plural = 'Livros do Ramon'
