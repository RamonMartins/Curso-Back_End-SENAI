from django.shortcuts import render
from .models import *

def ProdutoView(request, id):
    busca_produto = Produto.objects.get(id=id)
    return render(request, 'detalhes_produto.html', {'produto':busca_produto})
