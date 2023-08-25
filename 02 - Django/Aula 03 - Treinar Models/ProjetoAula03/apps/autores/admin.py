from django.contrib import admin
from .models import *
from apps.livros.models import Livro

#admin.site.register(Autor)

class LivroInline(admin.TabularInline):
    model = Livro
    extra = 0  # Número de campos de livro adicionais a serem exibidos

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    inlines = [LivroInline]
