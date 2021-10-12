from django.db import models
from produtos.models import Fornecedor


class Venda(models.Model):
    cod_venda = models.AutoField(primary_key=True)
    data_venda = models.DateField()
    valor_total_venda = models.FloatField()
    cnpj = models.ForeignKey(Fornecedor, models.DO_NOTHING, db_column='cnpj', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'venda'


class ItensVenda(models.Model):
    cod_item_venda = models.AutoField(primary_key=True)
    quantidade = models.IntegerField()
    valor_unit_venda = models.FloatField()
    cod_produto = models.ForeignKey('Produto', models.DO_NOTHING, db_column='cod_produto')
    cod_venda = models.ForeignKey('Venda', models.DO_NOTHING, db_column='cod_venda')

    class Meta:
        managed = False
        db_table = 'itens_venda'

