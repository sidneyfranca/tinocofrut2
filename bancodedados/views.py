from django.shortcuts import render

from tinocofrut2.bancodedados.authentication import BearerTokenAuthentication
from .models import Produto, Estoque, Compra, Venda, Fiscal, RelatorioCompra, RelatorioVenda, CargaHoraria, Salario, Funcionario, FolhaDePonto

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Produto, Estoque, Compra, Venda, Fiscal, RelatorioCompra, RelatorioVenda
from rest_framework.decorators import authentication_classes
from rest_framework.permissions import IsAuthenticated

@authentication_classes([BearerTokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def cadastro_produtos(request):
    if request.method == 'POST':
        # Obtenha os dados do produto do corpo da requisição
        identificador = request.POST.get('identificador')
        quantidade_estoque = request.POST.get('quantidade_estoque')
        descricao = request.POST.get('descricao')
        nome = request.POST.get('nome')
        preco = request.POST.get('preco')
        categoria = request.POST.get('categoria')
        tipo = request.POST.get('tipo')

        # Crie um novo objeto de produto com os dados fornecidos
        produto = Produto.objects.create(identificador=identificador, quantidade_estoque=quantidade_estoque, descricao=descricao, nome=nome, preco=preco, categoria=categoria, tipo=tipo)

        # Obtenha os dados do estoque do corpo da requisição
        setor = request.POST.get('setor')
        corredor = request.POST.get('corredor')
        prateleira = request.POST.get('prateleira')

        # Crie um novo objeto de estoque relacionado ao produto
        Estoque.objects.create(setor=setor, corredor=corredor, prateleira=prateleira, produto=produto)

        return JsonResponse({'message': 'Produto cadastrado com sucesso!'})

@authentication_classes([BearerTokenAuthentication])
@permission_classes([IsAuthenticated])    
@csrf_exempt
def estoque_view(request):
    if request.method == 'POST':
        # Obtenha os dados da solicitação
        setor_id = request.POST.get('setor_id')
        corredor_id = request.POST.get('corredor_id')
        prateleira_id = request.POST.get('prateleira_id')
        produto_id = request.POST.get('produto_id')

        # Crie um novo objeto de estoque
        estoque = Estoque(setor_id=setor_id, corredor_id=corredor_id, prateleira_id=prateleira_id, produto_id=produto_id)
        estoque.save()

        return JsonResponse({'message': 'Estoque adicionado com sucesso.'})
    
@authentication_classes([BearerTokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def estoque_detalhe_view(request, estoque_id):
    try:
        estoque = Estoque.objects.get(id=estoque_id)

        # Retorne os detalhes do estoque em formato JSON
        return JsonResponse({'setor': estoque.setor.nome, 'corredor': estoque.corredor.nome, 'prateleira': estoque.prateleira.nome, 'produto': estoque.produto.nome})

    except Estoque.DoesNotExist:
        return JsonResponse({'error': 'Estoque não encontrado.'}, status=404)
    
@authentication_classes([BearerTokenAuthentication])
@permission_classes([IsAuthenticated])   
@csrf_exempt
def comprar_view(request):
    if request.method == 'POST':
        # Obtenha os dados da solicitação
        data = request.POST.get('data')
        valor_total = request.POST.get('valor_total')

        # Crie uma nova compra
        compra = Compra(data=data, valor_total=valor_total)
        compra.save()

        return JsonResponse({'message': 'Compra realizada com sucesso.'})
    
@authentication_classes([BearerTokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def vender_view(request):
    if request.method == 'POST':
        # Obtenha os dados da solicitação
        data = request.POST.get('data')
        valor_total = request.POST.get('valor_total')

        # Crie uma nova venda
        venda = Venda(data=data, valor_total=valor_total)
        venda.save()

        return JsonResponse({'message': 'Venda realizada com sucesso.'})
    
@authentication_classes([BearerTokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def fiscal_view(request):
    if request.method == 'POST':
        # Obtenha os dados da solicitação
        data = request.POST.get('data')
        descricao = request.POST.get('descricao')

        # Crie um novo registro fiscal
        fiscal = Fiscal(data=data, descricao=descricao)
        fiscal.save()

        return JsonResponse({'message': 'Registro fiscal adicionado com sucesso.'})

@authentication_classes([BearerTokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def relatorio_compra_view(request):
    # Obtenha os dados para gerar o relatório de compra
    # Por exemplo, filtre as compras por data e calcule o valor total

    # Retorne os dados do relatório em formato JSON
    return JsonResponse({'data': '2023-06-27', 'valor_total': 1000.0})

@authentication_classes([BearerTokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def relatorio_venda_view(request):
    # Obtenha os dados para gerar o relatório de venda
    # Por exemplo, filtre as vendas por data e calcule o valor total

    # Retorne os dados do relatório em formato JSON
    return JsonResponse({'data': '2023-06-27', 'valor_total': 1500.0})

@authentication_classes([BearerTokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def funcionario_view(request):
    if request.method == 'POST':
        # Obtenha os dados da solicitação
        nome = request.POST.get('nome')
        cargo_id = request.POST.get('cargo_id')
        setorFirma_id = request.POST.get('setorFirma_id')

        # Crie um novo funcionário
        funcionario = Funcionario(nome=nome, cargo_id=cargo_id, setorFirma_id=setorFirma_id)
        funcionario.save()

        return JsonResponse({'message': 'Funcionário cadastrado com sucesso.'})
    
@authentication_classes([BearerTokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def salario_view(request):
    if request.method == 'POST':
        # Obtenha os dados da solicitação
        funcionario_id = request.POST.get('funcionario_id')
        valor = request.POST.get('valor')

        # Crie um novo registro de salário
        salario = Salario(funcionario_id=funcionario_id, valor=valor)
        salario.save()

        return JsonResponse({'message': 'Registro de salário adicionado com sucesso.'})
    
@authentication_classes([BearerTokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def carga_horaria_view(request):
    if request.method == 'POST':
        # Obtenha os dados da solicitação
        funcionario_id = request.POST.get('funcionario_id')
        horas_semanais = request.POST.get('horas_semanais')

        # Crie um novo registro de carga horária
        carga_horaria = CargaHoraria(funcionario_id=funcionario_id, horas_semanais=horas_semanais)
        carga_horaria.save()

        return JsonResponse({'message': 'Registro de carga horária adicionado com sucesso.'})

@authentication_classes([BearerTokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def folha_ponto_view(request):
    if request.method == 'POST':
        # Obtenha os dados da solicitação
        funcionario_id = request.POST.get('funcionario_id')
        data = request.POST.get('data')
        horas_trabalhadas = request.POST.get('horas_trabalhadas')



