from rest_framework.serializers import ModelSerializer
from veiculos.models import Veiculos


class VeiculosSerializer(ModelSerializer):
    class Meta:
        model = Veiculos
        fields = ('Marca', 'Modelo', 'Cor', 'Placa', 'is_especial')