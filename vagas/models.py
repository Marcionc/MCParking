
from django.db import models
from veiculos.models import Veiculos
from estacionamento.models import Estacionamento

class Vagas(models.Model):

    placa = models.ForeignKey(Veiculos, on_delete=models.CASCADE)
    nome = models.ForeignKey(Estacionamento, on_delete=models.CASCADE,verbose_name='Estacionamento')
    date_in = models.DateTimeField('Data de Entrada', auto_now=True)
    date_pay = models.DateTimeField('Data do Pagamento', auto_now=False)
    date_out = models.DateTimeField('Data de Saida', auto_now=False)
    value = models.IntegerField('Valor Pago')

    class Meta:
        verbose_name_plural = 'Vagas'

    def __str__(self):
        return f"TKT-{self.id}"
