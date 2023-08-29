from django.urls import path
from . import views

urlpatterns = [
    #path('apresentacao/', views.saudacao, name='ola_usuario')
    path('', views.saudacao, name='ola_usuario')
]
