from django.contrib import admin
from bancodedados import models
# Register your models here.

admin.site.register(models.Produto)
admin.site.register(models.Estoque)
admin.site.register(models.Compra)
admin.site.register(models.Venda)
admin.site.register(models.Fiscal)
admin.site.register(models.RelatorioCompra)
admin.site.register(models.RelatorioVenda)
admin.site.register(models.CargaHoraria)
admin.site.register(models.FolhaDePonto)
admin.site.register(models.Salario)
admin.site.register(models.Funcionario)