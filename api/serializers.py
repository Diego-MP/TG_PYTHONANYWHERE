from dataclasses import field
from rest_framework import serializers
from api import models

class ProdutosSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Produtos
        fields = '__all__'

class ClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Clientes
        fields = '__all__'
        #exclude = []

class ChamadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Chamados
        fields = '__all__'

class OrdensDeServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrdensDeServico
        fields = '__all__'

class PedidoDeVendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PedidoDeVenda
        fields = '__all__'

class PedidoProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PedidoProduto
        fields = '__all__'
