from django.shortcuts import render
from .models import *

# Create your views here.
def blog(request):
    lista_noticias = Noticia.objects.all()
    dados = {
        "noticias":lista_noticias
        }
    return render(request, "blog.html", dados)

def DetailsBlog(request, id):
    busca_id = Noticia.objects.get(id=id)
    dados = {
        "noticia": busca_id
    }
    return render(request, "blog_details.html", dados)
