from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from veiculos.models import Veiculos
from .serializers import VeiculosSerializer


class VeiculosViewSet(ModelViewSet):
    queryset = Veiculos.objects.all()
    serializer_class = VeiculosSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication, )
