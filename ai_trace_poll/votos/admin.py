from django.contrib import admin
from .models import Imagem, UsuarioVotante, Voto


@admin.register(Imagem)
class ImagemAdmin(admin.ModelAdmin):
    list_display = ('id', 'origem', 'arquivo')
    list_filter = ('origem',)
    search_fields = ('id',)
    ordering = ('id',)


@admin.register(UsuarioVotante)
class UsuarioVotanteAdmin(admin.ModelAdmin):
    list_display = ('email', 'votou_em')
    search_fields = ('email',)
    ordering = ('-votou_em',)


@admin.register(Voto)
class VotoAdmin(admin.ModelAdmin):
    list_display = ('email', 'imagem', 'resposta', 'acertou')
    list_filter = ('resposta', 'acertou')
    search_fields = ('email__email', 'imagem__id')
    ordering = ('email',)