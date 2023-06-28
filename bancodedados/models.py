from django.db import models

# Create your models here.

class Produto(models.Model):

    identificador = models.AutoField(primary_key=True)
    quantidade = models.PositiveIntegerField()
    descricao = models.TextField()
    nome = models.CharField(max_length=50)

    def _str_(self):

        return self.nome

from django.db import models

class Setor(models.Model):
    nome = models.CharField(max_length=100)

class Corredor(models.Model):
    nome = models.CharField(max_length=100)

class Prateleira(models.Model):
    nome = models.CharField(max_length=100)

class Estoque(models.Model):
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE)
    corredor = models.ForeignKey(Corredor, on_delete=models.CASCADE)
    prateleira = models.ForeignKey(Prateleira, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)

class Compra(models.Model):
    data = models.DateField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)

class Venda(models.Model):
    data = models.DateField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)

class Fiscal(models.Model):
    data = models.DateField()
    descricao = models.TextField()

class RelatorioCompra(models.Model):
    data = models.DateField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)

class RelatorioVenda(models.Model):
    data = models.DateField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)

class Compra(models.Model):
    data = models.DateField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)

class Venda(models.Model):
    data = models.DateField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)

class Fiscal(models.Model):
    data = models.DateField()
    descricao = models.TextField()

class RelatorioCompra(models.Model):
    data = models.DateField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)

class RelatorioVenda(models.Model):
    data = models.DateField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)

class SetorFirma(models.Model):
    nome = models.CharField(max_length=100)

class Cargo(models.Model):
    nome = models.CharField(max_length=100)

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE)

class Salario(models.Model):
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

class CargaHoraria(models.Model):
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    horas_semanais = models.IntegerField()

class FolhaDePonto(models.Model):
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    data = models.DateField()
    horas_trabalhadas = models.DecimalField(max_digits=5, decimal_places=2)