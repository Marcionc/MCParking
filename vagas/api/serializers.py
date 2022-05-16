from rest_framework.serializers import ModelSerializer
from vagas.models import Vagas


class VagasSerializer(ModelSerializer):
    class Meta:
        model = Vagas
        fields = ('placa', 'nome', 'date_in', 'date_pay', 'date_out', 'value')

