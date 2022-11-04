from django.contrib import admin
from api import models

#COMO SERA EXIBIDO NO ADMIN
class Produto(admin.ModelAdmin):
    list_display = ('id', 'nome', 'descricao') #campos a serem exibidos no admon
    list_display_link = ('id', 'nome') #campo clicaveis e editaveis
    search_fields = ('nome',) #busca por campo TUPLE
    list_per_page = 10 #itens por pagina

admin.site.register(models.Produtos, Produto)

class Cliente(admin.ModelAdmin):
    list_display = ('id', 'numero_identificacao', 'nome')
    list_display_link = ('id', 'numero_identificacao', 'nome')
    search_fields = ('nome',) #busca por campo
    list_per_page = 10 #itens por pagina

admin.site.register(models.Clientes, Cliente)

class Chamado(admin.ModelAdmin):

    list_display_link = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 10

admin.site.register(models.Chamados, Chamado)

class OrdemDeServico(admin.ModelAdmin):
    list_display = ('id', 'chamado', 'equipamento')
    list_display_link = ('id', 'chamado')
    search_fields = ('nome',)
    list_per_page = 10

admin.site.register(models.OrdensDeServico, OrdemDeServico)

class PedidoDeVenda(admin.ModelAdmin):
    #list_display = ('id', 'nome')
    #list_display_link = ('id', 'nome')
    #search_fields = ('nome',)
    list_per_page = 10

admin.site.register(models.PedidoDeVenda, PedidoDeVenda)

class PedidoProduto(admin.ModelAdmin):
    #list_display = ('id_pedido')
    #list_display_link = ('id_pedido',)
    #search_fields = ('nome',)
    list_per_page = 10

admin.site.register(models.PedidoProduto, PedidoProduto)