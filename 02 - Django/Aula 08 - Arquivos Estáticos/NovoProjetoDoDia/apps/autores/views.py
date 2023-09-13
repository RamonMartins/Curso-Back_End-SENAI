from django.shortcuts import render
from .models import Autor

def AutoresView(request):
    autores_lista = Autor.objects.all()
    return render(request, "index.html", {'nome_autores':autores_lista})

