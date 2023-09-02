from django.shortcuts import render
from .models import Produto

def ProdutosView(request):
    produtos_lista = Produto.objects.all()
    return render(request, 'produtos/index.html', {'produtos':produtos_lista})
