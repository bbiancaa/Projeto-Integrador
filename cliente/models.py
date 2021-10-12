from django.db import models


class Cliente(models.Model):
    cpf = models.CharField(primary_key=True, max_length=11)
    nome_cliente = models.CharField(max_length=50)
    telefone_cliente = models.IntegerField()
    cidade_cliente = models.CharField(max_length=50)
    bairro_cliente = models.CharField(max_length=50)
    rua_cliente = models.CharField(max_length=50)
    numero_cliente = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cliente'
