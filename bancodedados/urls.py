from django.urls import path
from . import views

urlpatterns = [

    path('estoque/', views.estoque_view, name='estoque'),
    path('estoque/<int:estoque_id>/', views.estoque_detalhe_view, name='estoque_detalhe'),
    path('comprar/', views.comprar_view, name='comprar'),
    path('vender/', views.vender_view, name='vender'),
    path('fiscal/', views.fiscal_view, name='fiscal'),
    path('relatorio_compra/', views.relatorio_compra_view, name='relatorio_compra'),
    path('relatorio_venda/', views.relatorio_venda_view, name='relatorio_venda'),
    path('funcionario/', views.funcionario_view, name='funcionario'),
    path('cargo/', views.cargo_view, name='cargo'),
    path('salario/', views.salario_view, name='salario'),
    path('carga-horaria/', views.carga_horaria_view, name='carga_horaria'),
    path('folha-ponto/', views.folha_ponto_view, name='folha_ponto'),
]

