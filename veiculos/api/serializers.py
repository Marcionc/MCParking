from rest_framework.serializers import ModelSerializer
from veiculos.models import Veiculos


class VeiculosSerializer(ModelSerializer):
    class Meta:
        model = Veiculos
        fields = ('marca', 'modelo', 'cor', 'placa', 'is_especial')