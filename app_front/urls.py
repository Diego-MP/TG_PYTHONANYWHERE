
from django.urls import path, include
from app_front import views

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.Home),
    path('home', views.Home, name='home'),
    path('listaclientes', views.listaClientes, name="listaclientes"),
    path('cadastrarcliente', views.cadastrarCliente, name="cadastrarcliente"),
    path('alterarcliente/<int:id>', views.alterarCliente, name="alterarcliente"),
    path('statusalterarcliente', views.statusAlterarCliente, name="statusalterarcliente"),
    path('apagarcliente/<int:id>', views.apagarCliente, name="apagarcliente"),
    path('cadastrarproduto', views.cadastrarProduto, name="cadastrarproduto"),
    path('listaprodutos', views.listaProdutos, name="listaprodutos"),
    path('alterarproduto/<int:id>', views.alterarProduto, name="alterarproduto"),
    path('apagarproduto/<int:id>', views.apagarProduto, name="apagarproduto"),
    path('statusalterarproduto', views.statusAlterarProduto, name="statusalterarproduto"),
    path('cadastrarchamado', views.cadastrarChamado, name="cadastrarchamado"),
    path('cadastrarchamado/<int:id>', views.cadastrarChamado, name="cadastrarchamado"),
    path('alterarchamado/<int:id>', views.alterarChamado, name="alterarchamado"),
    path('statusalterarchamado', views.statusAlterarChamado, name="statusalterarchamado"),
    path('listachamados', views.listaChamados, name="listachamados"),
    path('apagarchamado/<int:id>', views.apagarChamado, name="apagarchamado"),
    path('relatoriochamado/<int:id>', views.relatorioChamado, name="relatoriochamado"),

    path('cadastrarvenda', views.cadastrarVenda, name="cadastrarvenda"),

    path('adicionaprodutovendaatual', views.adicionaProdutoVendaAtual, name="adicionaprodutovendaatual"),
    path('listavendas', views.listaVendas, name="listavendas"),
    path('apagarvenda/<int:id>', views.apagarVenda, name="apagarvenda"),
    path('relatoriovenda/<int:id>', views.relatorioVenda, name="relatoriovenda"),

    path('cadastraros/<int:id>', views.cadastrarOS, name="cadastraros"),

    path('alteraros/<int:id>', views.alterarOS, name="alteraros"),
    path('statusalteraros', views.statusAlterarOS, name="statusalteraros"),

    path('login', views.login, name="login"),
    path('logoutsys', views.logout_sys, name="logoutsys"),    

    path('accounts/', include('django.contrib.auth.urls')),

    path('cadastrarlogin', views.cadastrarLogin, name="cadastrarlogin"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
