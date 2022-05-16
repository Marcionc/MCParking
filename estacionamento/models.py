from django.contrib.auth.models import User
from django.db import models

class Estacionamento(models.Model):

    nome = models.CharField('Nome', max_length=100)
    endereco = models.CharField('Endereço', max_length=200)
    total_vagas_comuns = models.IntegerField('Total de vagas comuns')
    total_vagas_especiais = models.IntegerField('Total de vagas especiais')
    vagas_livres_especiais = models.IntegerField('Vagas especiais livres')
    vagas_livres_comuns = models.IntegerField('Vagas comuns livres')

    class Meta:
        verbose_name_plural = 'Estacionamentos'


    def __str__(self):
        return self.nome
