from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from estacionamento.models import Estacionamento
from .serializers import EstacionamentoSerializer


class EstacionamentoViewSet(ModelViewSet):

    serializer_class = EstacionamentoSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        return Estacionamento.objects.all()
