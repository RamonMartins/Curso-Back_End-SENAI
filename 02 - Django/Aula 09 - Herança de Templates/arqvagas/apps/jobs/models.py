from django.db import models

# Create your models here.
class Job(models.Model):
    nome = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    cidade = models.CharField(max_length=50)
    qtd_jobs = models.IntegerField()

    def __str__(self):
        return self.nome