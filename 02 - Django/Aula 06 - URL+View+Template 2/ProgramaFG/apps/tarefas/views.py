from django.shortcuts import render
from .models import Tarefa


def TarefaView(request):
    lista_tarefas = Tarefa.objects.all()
    return render(request, 'index.html', {'tarefasArrey': lista_tarefas})
