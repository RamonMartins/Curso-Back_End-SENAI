from django.shortcuts import render

from .models import Job

# Create your views here.
def jobs(request):
    jobs = Job.objects.all()

    dados = {
        "jobs": jobs
        }
    return render(request, "jobs.html", dados)

def job(request, id):
    job = Job.objects.get(id=id)

    dados = {
        "job": job
    }

    return render(request, "vaga.html", dados)