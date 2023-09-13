from django.contrib import admin
from .models import *

#admin.site.register(Tarefa)

admin.site.site_header = 'Painel do JobsFG'

@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ("id", "titulo_tarefa", "descricao_tarefa", "status_tarefa")
    list_display_links = ("id",)
    list_editable = ("titulo_tarefa", "descricao_tarefa", "status_tarefa",)
    list_per_page = 2
    sortable_by = "-pk"
    list_filter = ("titulo_tarefa", "descricao_tarefa", "status_tarefa")
    search_fields = ("titulo_tarefa", "descricao_tarefa", "status_tarefa")

    