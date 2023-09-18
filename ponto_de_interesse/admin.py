from django.contrib import admin
from .models import Ponto_interesse

class PontoInteresseAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'descricao', 'caminho_imagem', 'localizacao')
    list_filter = ('localizacao',)  # Optional: Add filters for specific fields
    search_fields = ('nome', 'descricao')  # Optional: Add search fields

# Register your models here.
admin.site.register(Ponto_interesse, PontoInteresseAdmin)