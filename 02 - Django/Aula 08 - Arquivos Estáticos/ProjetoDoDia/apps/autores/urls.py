from django.urls import path
from . import views

urlpatterns = [
    		path('lista-autores/', views.AutoresView),
	    ]
