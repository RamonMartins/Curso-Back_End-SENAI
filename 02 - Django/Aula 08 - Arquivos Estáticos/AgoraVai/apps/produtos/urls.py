from django.urls import path
from .views import *

urlpatterns = [
    path('detalhes_produto/<int:id>', ProdutoView, name='ProdutosURL')
]
