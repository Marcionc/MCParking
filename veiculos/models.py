from django.contrib.auth.models import User
from django.db import models

class Veiculos(models.Model):

    marca = models.CharField('Marca', max_length=50, null=False)
    modelo = models.CharField('Modelo', max_length=50, null=False)
    cor = models.CharField('Cor', max_length=50, null=False)
    placa = models.CharField('Placa', max_length=8, null=False)
    is_ativo = models.BooleanField('Está estacionado?', default=False)
    is_especial = models.BooleanField('Necessita vaga especial?', default=False)
    is_plan = models.BooleanField('Possui plano ativo?', default=False)
    data_entrada = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Veiculos'

    def __str__(self):
        return self.placa
