from django.shortcuts import render
from apps.produtos.models import *

def HomeView(request):
    lista_produtos = Produto.objects.all()
    return render(request, 'index.html', {'produtos':lista_produtos})
