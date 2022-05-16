from rest_framework.viewsets import ModelViewSet
from veiculos.models import Veiculos
from .serializers import VeiculosSerializer


class VeiculosViewSet(ModelViewSet):
    queryset = Veiculos.objects.all()
    serializer_class = VeiculosSerializer
