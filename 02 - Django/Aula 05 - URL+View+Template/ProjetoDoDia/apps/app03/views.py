from django.shortcuts import render
from .models import *

def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/index.html', {'produtos': produtos})
