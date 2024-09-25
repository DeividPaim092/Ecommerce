from django.contrib import admin

from .models import Produto

admin.site.register(Produto)


class ProdutosAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nome', 'descricao',
                 'quantidade', 'valor', 'imagem')

