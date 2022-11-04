from django.contrib import admin
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
import requests
import json
from app_front import models as modelfront
from api import models
from django.core import serializers

# Create your views here.
@login_required(login_url='/login')
def Home(request):

    clientes_list = list()
    produtos_list = list()
    chamados_list = list()
    vendas_list = list()

    clientes = models.Clientes.objects.all()
    produtos = models.Produtos.objects.all()
    chamados = models.Chamados.objects.all()
    vendas = models.PedidoDeVenda.objects.all()
  
    for p in clientes:
        clientes_list.append(p)

    for p in produtos:
        produtos_list.append(p)

    for p in chamados:
        chamados_list.append(p)

    for p in vendas:
        vendas_list.append(p)

   
    print('------------')
    print(len(clientes_list))
    print(len(produtos_list))
    print(len(chamados_list))
    print(len(vendas_list))

    context = {
        'clientes_cadastrados': len(clientes_list),
        'produtos_cadastrados': len(produtos_list),
        'chamados_cadastrados': len(chamados_list),
        'vendas_cadastradas': len(vendas_list)
    }

    return render(request, 'app_front\pages\home.html', context=context)

@login_required(login_url='/login')
def listaClientes(request):
    response = requests.get("http://127.0.0.1:8000/api/clientes/").json()
    print(response)
    context = {
        'form': response
        }
    return render(request, 'app_front\pages\lista_clientes.html', context=context)

@login_required(login_url='/login')
def cadastrarCliente(request):

    form_sefaz = {}

    data_form = request.POST

    if request.method == 'POST' and data_form.get('btn_gravar', 'false')  == 'true':
        
       
       r = requests.post(f'http://127.0.0.1:8000/api/clientes/', data_form)
       print(r)
 
    elif request.method == 'POST' and data_form.get('btn_consultar_cnpj', 'false')  == 'true':
        print('consultando cnpj')

        
     
        cnpj = data_form.get('numero_identificacao', '')

        if cnpj == '':
            data_sefaz = {}
        else:
            data_sefaz = requests.get(f"https://minhareceita.org/{cnpj}/").json()

        
        
            form_sefaz = {
                'numero_identificacao': data_sefaz['cnpj'],
                'nome': data_sefaz['razao_social'],
                'apelido': data_sefaz['nome_fantasia'],
                'cep': data_sefaz['cep'],
                'cidade': data_sefaz['municipio'],
                'estado': data_sefaz['uf'],
                'endereco': data_sefaz['logradouro'],
                'numero': data_sefaz['numero'],
                'bairro': data_sefaz['bairro'],   
                'complemento': data_sefaz['complemento']
            }
            print('consultando cnpj')

    print(form_sefaz)
    context = {
        'form': form_sefaz,
        'button_context': "Gravar", #TROCA O NOME DO BOTAO DO TAMPLATE DE CADASTRAR CLIENTE DE GRAVAR PARA SALVAR|DEVIDO A SER UMA 
        'url_form_action': "/cadastrarcliente", #CONTROLA O ACTION DO FORM
        'method_form': 'POST',
        } 

    return render(request, 'app_front/pages/cadastro_cliente.html', context=context)

@login_required(login_url='/login')
def alterarCliente(request, id):

    response = requests.get(f"http://127.0.0.1:8000/api/clientes/{id}/").json()

    #CONTROLA SE O CHECK BOX ESTA TRUE OU FALSE E  CONVERTE PARA TAG HTML
    
    
    if response["tipo_cliente"] == True:
        response["tipo_cliente"] = "checked"
    elif response["tipo_cliente"] == False:
        response["tipo_cliente"] = ""
    
    if response["tipo_fornecedor"] == True:
        response["tipo_fornecedor"] = "checked"
    elif response["tipo_fornecedor"] == False:
        response["tipo_fornecedor"] = ""
    
    context = {
        'form': response,
        'button_context': "Salvar", #TROCA O NOME DO BOTAO DO TAMPLATE DE CADASTRAR CLIENTE DE GRAVAR PARA SALVAR|DEVIDO A SER UMA OPERAÇÃO DE UPDATE
        'url_form_action': "/statusalterarcliente", #CONTROLA O ACTION DO FORM
        'method_form': 'POST',  #CONTROLA METHOD DO FORM
        
        }                           

    #if request.method == 'POST':
        #print('post')

    print(response)
    
    return render(request, 'app_front/pages/cadastro_cliente.html', context=context)

@login_required(login_url='/login')
def statusAlterarCliente(request):
    if request.method == 'POST':

        id = request.POST['id']
        data_form = request.POST
        
        '''
        data_form_matable = data_form.copy()

        if data_form_matable["check_cliente"] == 'on':
            data_form_matable["check_cliente"] = True
        elif data_form_matable["check_cliente"] == '':
            data_form_matable["check_cliente"] = False
        
        if data_form_matable["check_fornecedor"] == 'on':
            data_form_matable["check_fornecedor"] = True
        elif data_form_matable["check_fornecedor"] == '':
            data_form_matable["check_fornecedor"] = False
        '''
        r = requests.put(f'http://127.0.0.1:8000/api/clientes/{id}/', data_form)
        print(r)
 
        context = {
            'form': data_form,
            'message': 'Cliente Alterado com sucesso | colocar btn de voltar a listagem',
        }
    else:
        print('diferente de POST')

    return render(request, 'app_front/pages/mensagem.html', context=context)

@login_required(login_url='/login')
def apagarCliente(request, id):
    if request.method == 'POST':

        
        r = requests.delete(f'http://127.0.0.1:8000/api/clientes/{id}/')
        print(r)
 
        
    else:
        print('diferente de POST')
    
        r = requests.delete(f'http://127.0.0.1:8000/api/clientes/{id}/')
        print(r)

    context = {
            'form': '',
            'message': 'Cliente Excluido com sucesso | colocar btn de voltar a listagem',
        }

    return render(request, 'app_front/pages/mensagem.html', context=context)
    #return redirect('app_front/pages/lista_clientes.html')

@login_required(login_url='/login')
def cadastrarProduto(request):
    if request.method == 'POST':
        
       data_form = request.POST
      # img_form = request.FILES['imagem']
       #file_form = request.FILES
       #data_form['imagem'] = "http://127.0.0.1:8000/media/img_produtos/" + data_form['imagem']
       r = requests.post(f'http://127.0.0.1:8000/api/produtos/', data_form)
       print(r)
        
       #print(json.dumps(r, indent = 1))
    
    context = {
        'form': '',
        'button_context': "Gravar", #TROCA O NOME DO BOTAO DO TAMPLATE DE CADASTRAR CLIENTE DE GRAVAR PARA SALVAR|DEVIDO A SER UMA 
        'url_form_action': "/cadastrarproduto", #CONTROLA O ACTION DO FORM
        'method_form': 'POST',
        } 
    return render(request, 'app_front/pages/cadastro_produtos.html', context=context)

@login_required(login_url='/login')
def listaProdutos(request):
    response = requests.get("http://127.0.0.1:8000/api/produtos/").json()
    print(response)
    context = {
        'form': response
        }
    return render(request, 'app_front\pages\lista_produtos.html', context=context)

@login_required(login_url='/login')
def alterarProduto(request, id):
    response = requests.get(f"http://127.0.0.1:8000/api/produtos/{id}/").json()
    #img_url = response['imagem']
    #img_url = img_url.lstrip("http://127.0.0.1:8000")
    #response['imagem'] = img_url

    form_img = response['imagem_name']
    context = {
        'form': response,
        'form_ig': form_img,
        'button_context': "Salvar", #TROCA O NOME DO BOTAO DO TAMPLATE DE CADASTRAR CLIENTE DE GRAVAR PARA SALVAR|DEVIDO A SER UMA OPERAÇÃO DE UPDATE
        'url_form_action': "/statusalterarproduto", #CONTROLA O ACTION DO FORM
        'method_form': 'POST',  #CONTROLA METHOD DO FORM
        }                           

    print(response)
    
    return render(request, 'app_front/pages/cadastro_produtos.html', context=context)

@login_required(login_url='/login')
def apagarProduto(request, id):
    if request.method == 'POST':

        
        r = requests.delete(f'http://127.0.0.1:8000/api/produtos/{id}/')
        print(r)
 
        
    else:
        print('diferente de POST')
    
        r = requests.delete(f'http://127.0.0.1:8000/api/produtos/{id}/')
        print(r)

    context = {
            'form': '',
            'message': 'Produto Excluido com sucesso | colocar btn de voltar a listagem',
        }

    return render(request, 'app_front/pages/mensagem.html', context=context)

@login_required(login_url='/login')
def statusAlterarProduto(request):
    if request.method == 'POST':

        id = request.POST['id']
        data_form = request.POST
        
        r = requests.put(f'http://127.0.0.1:8000/api/produtos/{id}/', data_form)
        print(r)
 
        context = {
            'form': data_form,
            'message': 'Cliente Alterado com sucesso | colocar btn de voltar a listagem',
        }
    else:
        print('diferente de POST')

    return render(request, 'app_front/pages/mensagem.html', context=context)

@login_required(login_url='/login')
def cadastrarChamado(request, id=0):
    #carrega os clientes opara preencher o campo de cliente
    response = requests.get("http://127.0.0.1:8000/api/clientes/").json()
    
    cliente = requests.get(f"http://127.0.0.1:8000/api/clientes/{id}/").json()
    print(json.dumps(cliente, indent = 1))
    if request.method == 'POST':
        
       data_form = request.POST
       r = requests.post(f'http://127.0.0.1:8000/api/chamados/', data_form)

    
       print(json.dumps(data_form, indent = 1))
       #print(data_form)

    context = {
        'form': response,
        'form_cliente': cliente,
        'button_context': "Gravar", #TROCA O NOME DO BOTAO DO TAMPLATE DE CADASTRAR CLIENTE DE GRAVAR PARA SALVAR|DEVIDO A SER UMA OPERAÇÃO DE UPDATE
        'url_form_action': "/cadastrarchamado", #CONTROLA O ACTION DO FORM
        'method_form': 'POST',  #CONTROLA METHOD DO FORM
        }
    return render(request, 'app_front/pages/cadastro_chamado.html', context=context)

@login_required(login_url='/login')
def alterarChamado(request, id):
    chamado = requests.get(f"http://127.0.0.1:8000/api/chamados/{id}/").json()

    
    clientes = requests.get("http://127.0.0.1:8000/api/clientes/").json()
    
    cliente_id = chamado['cliente']

    #for chamado in chamados:
    for cliente in clientes:
        if chamado['cliente'] == cliente['id']:
            chamado['cliente'] = cliente
        else:
            pass
    
    
    #cliente_id = chamado['cliente']
    print(cliente_id)
    cliente = requests.get(f"http://127.0.0.1:8000/api/clientes/{cliente_id}/").json()

    print(clientes)
    context = {
        'form': chamado,
        'form_clientes': clientes,
        'form_cliente': cliente,
        'button_context': "Salvar", #TROCA O NOME DO BOTAO DO TAMPLATE DE CADASTRAR CLIENTE DE GRAVAR PARA SALVAR|DEVIDO A SER UMA OPERAÇÃO DE UPDATE
        'url_form_action': "/statusalterarchamado", #CONTROLA O ACTION DO FORM
        'method_form': 'POST',  #CONTROLA METHOD DO FORM
        #'block_select': 'disabled'
        }                           

   
    
    return render(request, 'app_front/pages/cadastro_chamado.html', context=context)

@login_required(login_url='/login')
def statusAlterarChamado(request):
    if request.method == 'POST':

        id = request.POST['id']
        data_form = request.POST
        
        r = requests.put(f'http://127.0.0.1:8000/api/chamados/{id}/', data_form)
        print(r)

        print(json.dumps(data_form, indent = 1))
 
        context = {
            'form': data_form,
            'message': 'Chamado Alterado com sucesso | colocar btn de voltar a listagem',
        }
    else:
        print('diferente de POST')

    return render(request, 'app_front/pages/mensagem.html', context=context)

@login_required(login_url='/login')
def listaChamados(request):
    chamados = requests.get("http://127.0.0.1:8000/api/chamados/").json()
    clientes = requests.get("http://127.0.0.1:8000/api/clientes/").json()
    os = requests.get("http://127.0.0.1:8000/api/ordemservico/").json()
    
    print('---------------------------------------')
    print(type(chamados))

    list_chamados = []

    for chamado in chamados:
        for cliente in clientes:
            if chamado['cliente'] == cliente['id']:
                chamado['cliente'] = cliente
            else:
                pass

    for chamado in chamados:
        for o in os:
            if chamado['id'] == o['chamado']:
                chamado['status2'] = o['status2']
            else:
                pass
    print(json.dumps(chamados, indent = 1))

    for chamado in chamados:
        if chamado['status2'] == "Pendente":
            chamado['logo_status'] = '{0}'.format("/static/app_front/img/icons/Blue_Alert_128.png")
            
        
        elif chamado['status2'] == "Manutencao":
            chamado['logo_status'] = '{0}'.format("/static/app_front/img/icons/Yellow_Alert_128.png")
        
        elif chamado['status2'] == "Finalizada":
            chamado['logo_status'] =  '{0}'.format("/static/app_front/img/icons/Green_Alert_128.png")
        
        elif chamado['status2'] == "Reprovado":
            chamado['logo_status'] =  '{0}'.format("/static/app_front/img/icons/Red_Alert_128.png")
        
        elif chamado['status2'] == "":
            chamado['logo_status'] =  '{0}'.format("/static/app_front/img/icons/Blue_Alert_128.png")

        else:
            chamado['logo_status'] =  '{0}'.format("/static/app_front/img/icons/Blue_Alert_128.png")

        #print(chamado['logo_status'])

        list_chamados.append(chamado)

        #print('static "{0}"'.format("app_front/img/icons/Blue_Alert.png"))
       
        #print(json.dumps(chamado, indent = 1))

    context = {
        'form': list_chamados,
      
        }
    return render(request, 'app_front\pages\lista_chamados.html', context=context)

@login_required(login_url='/login')
def apagarChamado(request, id):
    if request.method == 'POST':

        
        r = requests.delete(f'http://127.0.0.1:8000/api/chamados/{id}/')
        print(r)
 
        
    else:
        print('diferente de POST')
    
        r = requests.delete(f'http://127.0.0.1:8000/api/chamados/{id}/')
        print(r)

    context = {
            'form': '',
            'message': 'Chamado Excluido com sucesso | colocar btn de voltar a listagem',
        }

    return render(request, 'app_front/pages/mensagem.html', context=context)

@login_required(login_url='/login')
def relatorioChamado(request, id=0):

    empresa = modelfront.Empresa.objects.all()
    chamado = requests.get(f'http://127.0.0.1:8000/api/chamados/{id}/').json()
    id_cliente = chamado['cliente']
    cliente = requests.get(f'http://127.0.0.1:8000/api/clientes/{id_cliente}/').json()
    os = requests.get("http://127.0.0.1:8000/api/ordemservico/").json()
    id_os = 0
    #print(f'id - {id}')
    
    for o in os:
        
        if str(o['chamado']) == str(id):
            id_os = o['id']
            
            
        else:
            pass
        
        
        print(o)    
        print(f'id da OS {id_os}')

    os_chamado = requests.get(f"http://127.0.0.1:8000/api/ordemservico/{id_os}/").json()


    #print(id_cliente)


    context = {
            'form': empresa,
            'form_chamado': chamado,
            'form_cliente': cliente,
            'form_os': os_chamado
            
    }
    return render(request, 'app_front/pages/relatorio_chamado.html', context=context)

@login_required(login_url='/login')
def cadastrarVenda (request, info = ''):
    '''
    try:
        if valor_total_venda in globals():
            pass
        else:
            valor_total_venda = list()

        if valor_total_venda in locals():
            pass
        else:
            valor_total_venda = list()
    except:
        pass
    finally:
        pass
    '''
    #carrega os clientes opara preencher o campo de cliente
    clientes = requests.get("http://127.0.0.1:8000/api/clientes/").json()
    produtos = requests.get("http://127.0.0.1:8000/api/produtos/").json()
    
    print(json.dumps(request.POST, indent = 1))

    data_form = request.POST
    

    
    if request.POST.get('btn_abrir_venda') == 'true':


        clientes = requests.get("http://127.0.0.1:8000/api/clientes/").json()
        produtos = requests.get("http://127.0.0.1:8000/api/produtos/").json()

        data_form = request.POST
        requests.post(f'http://127.0.0.1:8000/api/pedidovenda/', data_form)

        pedidos_vendas = requests.get("http://127.0.0.1:8000/api/pedidovenda/").json()
        ultimo_pedido_venda_id = pedidos_vendas[-1]['id']
        cliente_pedido_venda_id = pedidos_vendas[-1]['cliente']

        print(f'id venda: {ultimo_pedido_venda_id}')
        print(f'id cliente: {cliente_pedido_venda_id}')
        
        cliente = requests.get(f"http://127.0.0.1:8000/api/clientes/{cliente_pedido_venda_id}/").json()
        pedido_venda = requests.get(f"http://127.0.0.1:8000/api/pedidovenda/{ultimo_pedido_venda_id}/").json()
       

        print(f"Cliente: {cliente['nome']}")
        
        
        context = {
        'form_clientes': clientes,
        'form_cliente': cliente,
        'form_produtos': produtos,
        'form_pedido_venda': pedido_venda,
        'button_context': "Gravar", #TROCA O NOME DO BOTAO DO TAMPLATE DE CADASTRAR CLIENTE DE GRAVAR PARA SALVAR|DEVIDO A SER UMA OPERAÇÃO DE UPDATE
        'url_form_action': "/cadastrarvenda", #CONTROLA O ACTION DO FORM
        'method_form': 'POST',  #CONTROLA METHOD DO FORM
        'block_select': '',
        }

        return render(request, 'app_front/pages/cadastro_venda.html', context=context)

        #gerar um context com o cliente cadastradop e devolver a pagina com o 
        #clinete preenchido e campos de cliente desabilitados
       #set_cliente = True

    if request.POST.get('btn_add_produto') == 'true' :#and set cliente True
        #salva os produtos e devolve a pagina com o cliente e os produtos
        #quantidade = 1
        
        data_form = request.POST
        print(json.dumps(data_form, indent = 1))
       
        

        id_pedido = data_form['id']
        id_produto = data_form['produto']

        produto = requests.get(f'http://127.0.0.1:8000/api/produtos/{id_produto}/').json()

        '''
        if data_form.get('btn_gravar', 'false') == 'true' or data_form.get('btn_cancelar', 'false') == 'true':
            valor_total_venda = list()
        else:
            pass
        '''
        if data_form['valor_produto_adicionado'] == 'Padrao':
        
            preco_venda = produto['preco_venda']
            #preco_venda = data_form.get('valor_produto_adicionado', '0.00')
            #preco_venda = data_form('valor_produto_adicionado')
            #preco_venda = preco_venda.replace(',', '.')
        else:
            preco_venda = data_form['valor_produto_adicionado'].replace(',', '.')

       
        
        quantidade = data_form.get('quantidade_produto_adicionado', '0.00')
        #quantidade = data_form('quantidade_produto_adicionado')
        quantidade = quantidade.replace(',', '.')

        if quantidade == '':
            quantidade = 1
        else:
            pass


        preco_total = float(quantidade) * float(preco_venda) 

        #valor_total_venda.append(preco_total) 

        #valor_total_venda.append(preco_total)
        #preco_total = 100
    
        print(f'raw: {json.dumps(data_form, indent = 1)}')

        new_data_form = {
                "id_pedido": id_pedido,
                "id_produto": id_produto,
                "preco_venda": preco_venda,
                "quantidade": quantidade,
                "preco_total": preco_total
            }
        
        print(f'new: {json.dumps(new_data_form, indent = 1)}')

        requests.post(f'http://127.0.0.1:8000/api/pedidoproduto/', new_data_form)

        cliente_id = data_form['cliente']
        cliente = requests.get(f"http://127.0.0.1:8000/api/clientes/{cliente_id}/").json()

        pedido_venda_id = data_form['id']
        pedido_venda = requests.get(f"http://127.0.0.1:8000/api/pedidovenda/{pedido_venda_id}/").json()

        pedido_venda_produtos = models.PedidoProduto.objects.filter(id_pedido=pedido_venda_id).select_related()
        print(pedido_venda_produtos)

        
        #print(json.dumps(request.POST, indent = 1))

        valor_total_venda = 0
        for i in pedido_venda_produtos:
            pt = float(i.preco_total)
            valor_total_venda = valor_total_venda + pt
            

        context = {
        'form_clientes': clientes,
        'form_cliente': cliente,
        'form_produtos': produtos,
        'form_pedido_venda': pedido_venda,
        'valor_total_venda': valor_total_venda,
        'form_pedido_venda_produtos': pedido_venda_produtos,
        'button_context': "Gravar", #TROCA O NOME DO BOTAO DO TAMPLATE DE CADASTRAR CLIENTE DE GRAVAR PARA SALVAR|DEVIDO A SER UMA OPERAÇÃO DE UPDATE
        'url_form_action': "/cadastrarvenda", #CONTROLA O ACTION DO FORM
        'method_form': 'POST',  #CONTROLA METHOD DO FORM
        'block_select_product': '',
        'debug': ''#debug
        }

        return render(request, 'app_front/pages/cadastro_venda.html', context=context)


    context = {
        'form_clientes': clientes,
        'form_produtos': produtos,
        'button_context': "Gravar", #TROCA O NOME DO BOTAO DO TAMPLATE DE CADASTRAR CLIENTE DE GRAVAR PARA SALVAR|DEVIDO A SER UMA OPERAÇÃO DE UPDATE
        'url_form_action': "/cadastrarvenda", #CONTROLA O ACTION DO FORM
        'method_form': 'POST',  #CONTROLA METHOD DO FORM
        }

    return render(request, 'app_front/pages/cadastro_venda.html', context=context)

@login_required(login_url='/login')
def adicionaProdutoVendaAtual(request):

    if request.POST['btn_add_produto'] == 'true':
        id = request.POST

        print(json.dumps(id, indent = 1))
        print('add produto')

    else:
        print('outro')
    

    return render(request, 'app_front/pages/home.html')

@login_required(login_url='/login')
def listaVendas(request):
    pedidos_vendas = requests.get("http://127.0.0.1:8000/api/pedidovenda/").json()
    clientes = requests.get("http://127.0.0.1:8000/api/clientes/").json()
    #print(response)

    pedidos_vendas = models.PedidoDeVenda.objects.all().select_related()
    print(pedidos_vendas)


    context = {
        'form_pedidos_vendas': pedidos_vendas,
        }
        
    return render(request, 'app_front/pages/lista_vendas.html', context=context)

@login_required(login_url='/login')
def apagarVenda(request, id):
    requests.delete(f'http://127.0.0.1:8000/api/pedidovenda/{id}/')

    context = {
            'form': '',
            'message': 'Venda Excluida com sucesso | colocar btn de voltar a listagem',
        }

    return render(request, 'app_front/pages/mensagem.html', context=context)

@login_required(login_url='/login')
def relatorioVenda(request, id=0):
       
    empresa = modelfront.Empresa.objects.all()

    pedido_venda = models.PedidoProduto.objects.filter(id_pedido=id).select_related()
    
    #calcular o valor total de cada produto
    for i in pedido_venda:
       valor_total_produto = i.preco_venda * i.quantidade
       i.preco_total = valor_total_produto
    
    for i in pedido_venda:
        id_cliente = i.id_pedido.cliente.id
    
    cliente = requests.get(f'http://127.0.0.1:8000/api/clientes/{id_cliente}/').json()

    valor_total = 0
    for i in pedido_venda:
        valor_total = valor_total + (i.id_produto.preco_venda * i.quantidade)
        print(f'Valor Total: {valor_total}')
        print(f'Valor Total: {valor_total}')
    
    
    context = {
            'form': empresa,
            'form_pedido_venda': pedido_venda,
            'form_cliente': cliente ,
            'form_valor_total': valor_total,
            'valor_total_produto': valor_total_produto,
        }
    return render(request, 'app_front/pages/relatorio_venda.html', context=context)

@login_required(login_url='/login')
def cadastrarOS(request, id=0):
    
    chamado = requests.get(f'http://127.0.0.1:8000/api/chamados/{id}/').json()
    
    id_cliente = chamado['cliente']

    cliente = requests.get(f'http://127.0.0.1:8000/api/clientes/{id_cliente}/').json()

    produtos =  requests.get(f'http://127.0.0.1:8000/api/produtos/').json()


    context = {
        'form_cliente': cliente,
        'form_chamado': chamado,
        'form_produtos': produtos,
        'button_context': 'Gravar',
        'url_form_action': "", #CONTROLA O ACTION DO FORM
        'method_form': 'POST',  #CONTROLA METHOD DO FORM
            }

    if request.method == 'POST':
        
       data_form = request.POST

       new_data_form = {
                "equipamento": data_form['equipamento'],
                "peca": data_form['peca'],
                "numero_serie": data_form['numero_serie'],
                "valor": data_form['valor'],
                "tecnico": data_form['tecnico'],
                "observacao": data_form['observacao'],
                "chamado": data_form['id'],
                "status2": data_form['status2']
                    }
       
       print(f'RAW: {json.dumps(data_form, indent = 1)}')
       print(f'NEW: {json.dumps(new_data_form, indent = 1)}')
       requests.post(f'http://127.0.0.1:8000/api/ordemservico/', new_data_form)

       return redirect('listachamados')


    #print(json.dumps(chamado, indent = 1))
    return render(request, 'app_front/pages/cadastro_os.html', context=context)

@login_required(login_url='/login')
def alterarOS(request, id = 0):
    
    

    chamado_id = id
    os = models.OrdensDeServico.objects.filter(chamado=chamado_id).select_related()   

    os_list = list(os)

    
    cliente_id = os_list[0].chamado.cliente.id


        

    cliente = requests.get(f'http://127.0.0.1:8000/api/clientes/{cliente_id}/').json()


    context = {
        'form_os': os_list[0],
        'form_cliente': cliente,
        'button_context': "Salvar", #TROCA O NOME DO BOTAO DO TAMPLATE DE CADASTRAR CLIENTE DE GRAVAR PARA SALVAR|DEVIDO A SER UMA OPERAÇÃO DE UPDATE
        'url_form_action': "/statusalteraros", #CONTROLA O ACTION DO FORM
        'method_form': 'POST',  #CONTROLA METHOD DO FORM
    }
    

    return render(request, 'app_front\pages\cadastro_os_edit.html', context = context)

'''
def statusAlterarOS(request):
    if request.method == 'POST':

        id = request.POST['id_os']
        data_form = request.POST
        
        r = requests.put(f'http://127.0.0.1:8000/api/chamados/{id}/', data_form)
        print(r)

        print(json.dumps(data_form, indent = 1))
 
        context = {
            'form': data_form,
            'message': 'Chamado Alterado com sucesso | colocar btn de voltar a listagem',
        }
    else:
        print('diferente de POST')

    return render(request, 'app_front/pages/mensagem.html', context=context)
'''

@login_required(login_url='/login')
def statusAlterarOS(request):
   
        
        id = request.POST['id_os']
        print(f' A ID OS: {id}')
        id_bd_os = request.POST['id']

        data_form = request.POST

        if data_form['valor'].replace(',', '.') == 'None':
            new_valor = '0.00'
        else:
            new_valor = data_form['valor'].replace(',', '.')

        print(json.dumps(data_form, indent = 1))
        
        data_form_new = {
                "equipamento": data_form['equipamento'],
                "peca": data_form['peca'],
                "numero_serie": data_form['numero_serie'],
                "valor": new_valor,
                "tecnico": data_form['tecnico'],
                "status2": data_form['status2'],
                "observacao": data_form['observacao'],
                "chamado": data_form['id']
                }
        
        #requests.delete(f'http://127.0.0.1:8000/api/ordemservico/{id_bd_os}/')
        requests.put(f'http://127.0.0.1:8000/api/ordemservico/{id}/', data_form_new)
        
        print(data_form_new)

        
 
        context = {
            'form': data_form,
            'message': 'OS Alterado com sucesso | colocar btn de voltar a listagem',
        }


        return render(request, 'app_front/pages/mensagem.html', context=context)

def login (request):

    if request.method == "POST":
        username = request.POST["login_user"]
        password = request.POST["login_password"]
        print(f'{username} | {password}')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            auth_login(request, usuario)
            return render(request, 'app_front/pages/home.html')
        else: 
            pass


    
    return render(request, 'app_front/pages/login.html')

def logout_sys(request):
    
    auth_logout(request)
    
    return render(request, 'app_front/pages/mensagem_logout.html')

@login_required(login_url='/login')
def cadastrarLogin(request):

    data_form = request.POST
    usuario = data_form.get('usuario', '')
    senha = data_form.get('senha', '')

    if data_form.get('btn_gravar', 'false') == 'true':
        user_django = User.objects.create_user(username=usuario, password=senha)
        user_django.save()
    else:
        pass

    if data_form.get('btn_alterar', 'false') == 'true':
        user_django = User.objects.get(username=usuario)
        user_django.set_password(senha)
        user_django.save()
    else:
        pass
    
    print(f'{usuario} | {senha}')
    print(data_form)
    return render(request, 'app_front/pages/cadastro_user_login.html')