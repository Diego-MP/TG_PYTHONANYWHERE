from django.db import models

class Empresa(models.Model):

    id = models.AutoField(primary_key=True)
    #controlar na view quando 11 CPF e quando 14 cnpj menor que 11 RG
    numero_identificacao = models.CharField(verbose_name="RG/CPF/CNPJ", max_length=14, blank=True, null=True) #numero de digitos padrao em todos os estados BR
    
    nome = models.CharField(max_length=64)
    apelido = models.CharField(max_length=64, blank=True, null=True)

    cep = models.CharField(max_length=8, blank=True, null=True)
    cidade = models.CharField(max_length=64, blank=True, null=True)
    estado = models.CharField(max_length=64, blank=True, null=True)
    endereco = models.CharField(max_length=64, blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    complemento = models.CharField(max_length=64, blank=True, null=True)
    bairro = models.CharField(max_length=64, blank=True, null=True)

    telefone1 = models.CharField(max_length=32, blank=True, null=True)
    telefone2 = models.CharField(max_length=32, blank=True, null=True)
    whatsapp = models.CharField(max_length=32, blank=True, null=True)
    contato = models.CharField(max_length=32, blank=True, null=True)
    email = models.CharField(max_length=64, blank=True, null=True)
    site = models.CharField(max_length=64, blank=True, null=True)
    
    observacao = models.TextField(max_length=255, blank=True, null=True)

    data_criacao = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    data_modificacao = models.DateTimeField(auto_now=True, blank=True, null=True)

    #created_by = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nome

class VendaAUX(models.Model):
    
    id_venda = models.AutoField(primary_key=True)
    id_cliente = models.IntegerField(blank=True, null=True)
    id_produto = models.IntegerField(blank=True, null=True)
    valor = models.DecimalField(decimal_places=2, max_digits=9, blank=True, null=True)
    quantidade = models.IntegerField(blank=True, null=True)
    valor_total = models.DecimalField(decimal_places=2, max_digits=9, blank=True, null=True)

    def __str__(self):
        return (f'CHAMADO: {self.id_venda} - CLIENTE: {self.id_cliente}')