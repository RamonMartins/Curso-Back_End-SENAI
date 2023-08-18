from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.lista_tarefas, name='lista_tarefas'),
]
