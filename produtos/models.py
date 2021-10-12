from django.db import models
from django.urls import reverse
from cliente.models import Cliente

class Produto(models.Model):
    cod_produto = models.AutoField(primary_key=True)
    nome_produto = models.CharField(max_length=100)
    descr_produto = models.CharField(max_length=255)
    valor_unit = models.FloatField()
    quantidade = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'produto'

    def get_absolute_url(self):
        return reverse('product-list')
        # return reverse('product-update', kwargs={'pk': self.pk})


class Fornecedor(models.Model):
    cnpj = models.CharField(primary_key=True, max_length=14)
    nome_fantasia = models.CharField(max_length=50)
    razao_social = models.CharField(max_length=50)
    ie = models.IntegerField()
    email_fornecedor = models.CharField(max_length=100)
    telefone_fornecedor = models.IntegerField()
    cidade_fornecedor = models.CharField(max_length=50)
    bairro_fornecedor = models.CharField(max_length=50)
    rua_fornecedor = models.CharField(max_length=50)
    numero_fornecedor = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fornecedor'


class Compra(models.Model):
    cod_compra = models.AutoField(primary_key=True)
    data_compra = models.DateField()
    cpf = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cpf', blank=True, null=True)
    cod_produto = models.ForeignKey('Produto', models.DO_NOTHING, db_column='cod_produto')
    cnpj = models.ForeignKey('Fornecedor', models.DO_NOTHING, db_column='cnpj', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'compra'


