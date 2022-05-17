from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from vagas.models import Vagas
from .serializers import VagasSerializer


class VagasViewSet(ModelViewSet):

    serializer_class = VagasSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        return Vagas.objects.all()
