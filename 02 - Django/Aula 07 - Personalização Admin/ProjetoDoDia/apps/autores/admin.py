from django.contrib import admin
from .models import *
from apps.livros.models import Livro

#admin.site.register(Autor)

class LivroInline(admin.TabularInline):
    model = Livro
    extra = 0

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    inlines = (LivroInline,)
    list_display = ("id", "nome_autor", "idade_autor")
    list_display_links = ("id",)
    list_per_page = 4
    list_filter = ("idade_autor", "nome_autor")
    search_fields = ("nome_autor", "idade_autor")
