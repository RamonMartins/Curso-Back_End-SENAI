from django.contrib import admin
from .models import *
from apps.tarefas.models import Tarefa

class TarefaInline(admin.TabularInline):
    model = Tarefa
    extra = 0

@admin.register(Criador)
class CriadorAdmin(admin.ModelAdmin):
    inlines = (TarefaInline,)
    list_display = ("id", "nome_criador")
    list_display_links = ("id", "nome_criador")
    list_filter = ("id", "nome_criador", "idade_criador")
