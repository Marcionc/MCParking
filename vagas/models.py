
from django.db import models
from veiculos.models import Veiculos
from estacionamento.models import Estacionamento

class Vagas(models.Model):

    placa = models.ForeignKey(Veiculos, on_delete=models.CASCADE)
    nome = models.ForeignKey(Estacionamento, on_delete=models.CASCADE,
                             verbose_name='Estacionamento'
                             )
    is_ativa = models.BooleanField('Está ocupada?', default=True)
    is_pay = models.BooleanField('Está paga?', default=False)
    date_in = models.DateTimeField('Data de Entrada', blank=True, null=True)
    date_pay = models.DateTimeField('Data do Pagamento', blank=True, null=True)
    date_out = models.DateTimeField('Data de Saida', blank=True, null=True)
    value = models.IntegerField('Valor Pago', blank=True, null=True)

    class Meta:
        verbose_name = 'Vaga'
        verbose_name_plural = 'Vagas'

    def __str__(self):
        return f"TKT-{self.id}"
