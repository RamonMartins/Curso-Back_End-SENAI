from django.shortcuts import render

# Create your views here.
def jobs(request):
    dados = {
        "job":"Vaga de lutador de HTML"
        }
    return render(request, "jobs.html", dados)