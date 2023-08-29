from django.shortcuts import render

def saudacao(request):
    return render(request, 'saudacoes/ola_mundo.html')
