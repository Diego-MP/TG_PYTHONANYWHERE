from rest_framework import viewsets
from api import models
from api import serializers
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class ProdutosViewSet(viewsets.ModelViewSet):
    queryset = models.Produtos.objects.all()
    serializer_class = serializers.ProdutosSerializer
    #RESPONSAVEL PELO CONTROLE DE ACESSO
    #authentication_classes = [BasicAuthentication]
    #permission_classes = [IsAuthenticated]

class ClientesViewSet(viewsets.ModelViewSet):
    queryset = models.Clientes.objects.all()
    serializer_class = serializers.ClientesSerializer
    #RESPONSAVEL PELO CONTROLE DE ACESSO
    #authentication_classes = [BasicAuthentication]
    #permission_classes = [IsAuthenticated]

class ChamadosViewSet(viewsets.ModelViewSet):
    queryset = models.Chamados.objects.all()
    serializer_class = serializers.ChamadosSerializer
    #RESPONSAVEL PELO CONTROLE DE ACESSO
    #authentication_classes = [BasicAuthentication]
    #permission_classes = [IsAuthenticated]

class OrdensDeServicoViewSet(viewsets.ModelViewSet):
    queryset = models.OrdensDeServico.objects.all()
    serializer_class = serializers.OrdensDeServicoSerializer
    #RESPONSAVEL PELO CONTROLE DE ACESSO
    #authentication_classes = [BasicAuthentication]
    #permission_classes = [IsAuthenticated]

class PedidoDeVendaViewSet(viewsets.ModelViewSet):
    queryset = models.PedidoDeVenda.objects.all()
    serializer_class = serializers.PedidoDeVendaSerializer
    #RESPONSAVEL PELO CONTROLE DE ACESSO
    #authentication_classes = [BasicAuthentication]
    #permission_classes = [IsAuthenticated]

class PedidoProdutoViewSet(viewsets.ModelViewSet):
    queryset = models.PedidoProduto.objects.all()
    serializer_class = serializers.PedidoProdutoSerializer
    #RESPONSAVEL PELO CONTROLE DE ACESSO
    #authentication_classes = [BasicAuthentication]
    #permission_classes = [IsAuthenticated]
