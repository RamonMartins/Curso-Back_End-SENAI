from django.shortcuts import render

# Create your views here.
def candidate(request):
    dados = {
        "candidato":"Jaelito o lutador"
        }
    return render(request, "candidate.html", dados)