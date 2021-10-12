from django.db import models


class Usuario(models.Model):
    cod_usuario = models.AutoField(primary_key=True)
    nome_usuario = models.CharField(max_length=50)
    email_usuario = models.CharField(max_length=100)
    senha_usuario = models.CharField(max_length=20)
    usuario_adm = models.BooleanField(blank=True, null=True)
    usuario_colaborador = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario'

