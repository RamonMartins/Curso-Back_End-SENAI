from django.shortcuts import render

# Create your views here.
def blog(request):
    dados = {
        "noticia":"Jaelito vira lutador"
        }
    return render(request, "blog.html", dados)