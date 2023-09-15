from django.shortcuts import render
from apps.produtos.models import *

def HomePage(request):
    lista_produtos = Produto.objects.all()
    return render(request, 'home.html', {'produtos':lista_produtos})
