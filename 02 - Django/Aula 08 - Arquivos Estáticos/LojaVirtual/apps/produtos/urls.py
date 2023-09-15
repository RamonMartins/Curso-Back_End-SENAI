from django.urls import path
from .views import *

urlpatterns = [
    path('produto/<int:id>/', ProdutoView, name='ProdutosURL'),
]
