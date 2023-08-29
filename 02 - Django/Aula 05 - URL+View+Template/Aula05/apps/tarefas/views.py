from django.shortcuts import render
from .models import Tarefa
#from django.http import HttpResponse

#def saudacao(request):
#    return HttpResponse("Olá mundo!!!")

#def saudacao(request):
#    return render(request, 'saudacoes/ola_mundo.html')

def saudacao(request):
    tupla_tarefas = ["lavar carro", "limpar casa", "fazer feira"]
    return render(request, 'saudacoes/lista_tarefas.html', {'tarefas': tupla_tarefas})
