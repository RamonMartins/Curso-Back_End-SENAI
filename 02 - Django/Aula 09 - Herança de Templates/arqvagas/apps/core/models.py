from django.db import models

# Create your models here.
class Configuracao(models.Model):
    slogan = models.CharField(max_length=50)
    nome_empresa = models.CharField(max_length=20)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.nome_empresa