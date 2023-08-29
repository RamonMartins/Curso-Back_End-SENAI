from django.db import models

class Tarefa(models.Model):
    descricao_tarefa = models.CharField(max_length=200)
    concluida = models.BooleanField(default=False)

    def __str__(self):
        return self.descricao_tarefa
