from django.db import models

class Tarefa(models.Model):
    responsavel_tarefa = models.ForeignKey("criadores.Criador", on_delete=models.CASCADE, null=True, blank=True)
    titulo_tarefa = models.CharField(max_length=200, verbose_name="Título da Tarefa")
    descricao_tarefa = models.TextField()
    status_tarefa = models.BooleanField(default=False, verbose_name="Concluído")

    def __str__(self):
        return self.titulo_tarefa
    
    class Meta:
        verbose_name = "Tarefassss"
