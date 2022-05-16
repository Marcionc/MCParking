from rest_framework.serializers import ModelSerializer
from estacionamento.models import Estacionamento


class EstacionamentoSerializer(ModelSerializer):
    class Meta:
        model = Estacionamento
        fields = ('nome', 'endereco', 'vagas_livres_comuns', 'vagas_livres_especiais')
