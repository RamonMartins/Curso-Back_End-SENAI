from django.shortcuts import render

def saudacao(request):
    lista_tarefas = ["limpar casa", "limpar carro", "fazer feira"]
    return render(request, 'saudacoes/ola_mundo.html', {'tarefas':lista_tarefas})
