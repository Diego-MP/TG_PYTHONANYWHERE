
from django.urls import path, include

#from recipes_app.views import home, contato
#para importar tudo
from api import views
#OU USANDO PONTO .
#from . import views # da pasta que estou import views
#chamados devem ser feitas por views.funcao
from rest_framework import routers


#Registra as urls para acesso da api pelo root
router = routers.DefaultRouter()
router.register('produtos', views.ProdutosViewSet, basename='Produtos')
router.register('clientes', views.ClientesViewSet, basename='Clientes')
router.register('chamados', views.ChamadosViewSet, basename='Chamados')
router.register('ordemservico', views.OrdensDeServicoViewSet, basename='OrdemDeServico')
router.register('pedidovenda', views.PedidoDeVendaViewSet, basename='PedidoDeVenda')
router.register('pedidoproduto', views.PedidoProdutoViewSet, basename='PedidoVenda')


urlpatterns = [
    path('', include(router.urls)),
]