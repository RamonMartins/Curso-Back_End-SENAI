from django.urls import path
from . import views

urlpatterns = [
    path('lista-produtos', views.ProdutosView, name='lista_de_produtos')
]
