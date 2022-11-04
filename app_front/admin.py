from django.contrib import admin
from app_front import models

class Empresa(admin.ModelAdmin):
    list_display = ('id', 'numero_identificacao', 'nome')
    list_display_link = ('id', 'numero_identificacao', 'nome')
    search_fields = ('nome',) #busca por campo
    list_per_page = 10 #itens por pagina

admin.site.register(models.Empresa, Empresa)
