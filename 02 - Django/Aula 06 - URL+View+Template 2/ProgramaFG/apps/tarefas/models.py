from django.db import models

class Tarefa(models.Model):
    titulo_tarefa = models.CharField(max_length=200)
    descricao_tarefa = models.TextField()
    status_tarefa = models.BooleanField(default=False, verbose_name="Concluído")

    def __str__(self):
        return self.titulo_tarefa
