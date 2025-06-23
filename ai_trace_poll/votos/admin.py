from django.contrib import admin
from .models import Imagem, UsuarioVotante, Voto


@admin.register(Imagem)
class ImagemAdmin(admin.ModelAdmin):
    list_display = ('id', 'origem', 'preview')
    list_filter = ('origem',)
    search_fields = ('id',)
    ordering = ('id',)

    def preview(self, obj):
        if obj.arquivo:
            return f'<img src="{obj.arquivo.url}" style="height:50px;"/>'
        return 'Sem imagem'

    preview.allow_tags = True
    preview.short_description = 'Preview'


@admin.register(UsuarioVotante)
class UsuarioVotanteAdmin(admin.ModelAdmin):
    list_display = ('email', 'votou_em')
    search_fields = ('email',)
    ordering = ('-votou_em',)


@admin.register(Voto)
class VotoAdmin(admin.ModelAdmin):
    list_display = ('email', 'imagem', 'resposta')
    list_filter = ('resposta',)
    search_fields = ('email__email', 'imagem__id')
    ordering = ('email',)