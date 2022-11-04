from distutils.command.upload import upload
from django.db import models

class Produtos(models.Model):

    UNIDADES_CHOICES = (
        ("UN", "Unidade"),
        ("PT", "Pacote"),
        ("KT", "Kit"),
        ("PC", "Peça"),
        ("KG", "Quilograma"),
        ("MT", "Metro")
    )

    MOBILIZACAO_CHOICES = (
        ("REP", "Reposicao"),
        ("VND", "Venda"),
        ("GNT", "Garantia"),
    )

    id = models.AutoField(primary_key=True)

    nome = models.CharField(max_length=64) #futuramente pode haver acrescimo de digitos acima de 9
    codigo_interno = models.CharField(max_length=13, blank=True, null=True) #numero de digitos padrao em todos os estados BR
    codigo_barras = models.CharField(max_length=13, blank=True, null=True)
    unidade = models.CharField(max_length=64, choices=UNIDADES_CHOICES, blank=True, null=True)
    marca = models.CharField(max_length=64, blank=True, null=True)
    modelo = models.CharField(max_length=64, blank=True, null=True)
    preco_custo = models.DecimalField(decimal_places=2, max_digits=9, blank=True, null=True)
    preco_venda = models.DecimalField(decimal_places=2, max_digits=9, blank=True, null=True)
    estoque = models.IntegerField(blank=True, null=True)
    grupo = models.CharField(max_length=64, blank=True, null=True)
    descricao = models.TextField(max_length=255, blank=True, null=True)
    fornecedor = models.CharField(max_length=64, blank=True, null=True)
    mobilizacao = models.CharField(max_length=3, choices=MOBILIZACAO_CHOICES, blank=True, null=True)
    imagem = models.ImageField(upload_to = 'img_produtos/', blank=True, null=True)
    imagem_name = models.CharField(max_length=64, blank=True, null=True)

    data_criacao = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    data_modificacao = models.DateTimeField(auto_now=True, blank=True, null=True)
    

    def __str__(self):
        return self.nome

class Clientes(models.Model):

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
    
    observacao = models.TextField(max_length=255, blank=True, null=True)

    tipo_cliente = models.BooleanField(verbose_name="É Cliente", default=False, blank=True, null=True)
    tipo_fornecedor = models.BooleanField(verbose_name="É Fornecedor", default=False, blank=True, null=True)

    data_criacao = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    data_modificacao = models.DateTimeField(auto_now=True, blank=True, null=True)

    #created_by = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nome

class Chamados(models.Model):

    STATUS_CHOICES = (
        ("1", "Pendente"),
        ("2", "Manutencao"),
        ("3", "Finalizada"),
        ("4", "Reprovado")
    )

    id = models.AutoField(primary_key=True)
    #CASO O CLIENTE FOR APAGADO TODOS OS CHAMADO REFERENTE A ELE TMBEM SERAO
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    defeito = models.TextField(max_length=255, blank=True, null=True)

    telefone_chamado = models.CharField(max_length=32, blank=True, null=True)
    contato_chamado = models.CharField(max_length=32, blank=True, null=True)

    status = models.CharField(max_length=2, choices=STATUS_CHOICES,blank=True, null=True)
    status2 = models.CharField(max_length=10 ,blank=True, null=True)
    logo_status = models.CharField(max_length=10 ,blank=True, null=True)

    data_criacao = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    data_modificacao = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return (f'{self.id} - {self.cliente.nome}')

class OrdensDeServico(models.Model):

    STATUS_CHOICES = (
        ("1", "Pendente"),
        ("2", "Manutencao"),
        ("3", "Finalizada"),
        ("4", "Reprovado")
    )

    id = models.AutoField(primary_key=True)

    chamado = models.ForeignKey(Chamados, on_delete=models.CASCADE)
    #produto = models.ManyToManyField(Produtos)

    equipamento = models.CharField(verbose_name="Equipamento", max_length=64, blank=True, null=True)
    peca = models.CharField(verbose_name="Peça", max_length=64, blank=True, null=True)
    numero_serie = models.CharField(verbose_name="N.Serie", max_length=64, blank=True, null=True)

    valor = models.DecimalField(decimal_places=2, max_digits=9, blank=True, null=True)
    #VER POSSIBILIDADE DE UMA TABELA FUNCIONARIO
    tecnico = models.CharField(verbose_name="Tecnico", max_length=64, blank=True, null=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES,blank=True, null=True)
    status2 = models.CharField(max_length=10 ,blank=True, null=True)

    observacao = models.TextField(max_length=255, blank=True, null=True)

    data_criacao = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    data_modificacao = models.DateTimeField(auto_now=True, blank=True, null=True)

class PedidoDeVenda(models.Model):
    id = models.AutoField(primary_key=True)

    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)

    telefone_venda = models.CharField(max_length=32, blank=True, null=True)
    contato_venda = models.CharField(max_length=32, blank=True, null=True)

    data_criacao = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    data_modificacao = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return (f'{self.id} - {self.cliente.nome}')

class PedidoProduto(models.Model):
    id_pedido = models.ForeignKey(PedidoDeVenda, on_delete=models.CASCADE)
    id_produto = models.ForeignKey(Produtos, on_delete=models.CASCADE)

    preco_venda = models.DecimalField(decimal_places=2, max_digits=9, blank=True, null=True)
    quantidade = models.IntegerField(blank=True, null=True)

    preco_total = models.DecimalField(decimal_places=2, max_digits=9, blank=True, null=True)


    def __str__(self):
        return (f'{self.id_pedido.id} - {self.id_pedido.cliente.nome} - {self.id_produto.nome}')

    