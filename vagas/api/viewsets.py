from django.views.generic import CreateView, UpdateView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from vagas.models import Vagas
from veiculos.models import Veiculos
from estacionamento.models import Estacionamento
from .serializers import VagasSerializer


class VagasViewSet(ModelViewSet):

    serializer_class = VagasSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['placa', 'nome']
    search_fields = ['placa', 'nome']

    def get_queryset(self):
        return Vagas.objects.all()

# Veiculo entra no estacionamento, gera data de entrada e marca que vaga esta ativa

class CriarVaga(CreateView):
    model = Vagas
    http_method_names = ['post']

    def Entrar(self, request, *args, **kwargs):
        if(Vagas.is_ativa==False):
            Vagas.is_ativa=True
        return

# Veiculo registra pagamento, marca que está pago e libera para saida

class PagarVaga(UpdateView):
    model = Vagas
    http_method_names = ['post']

    def Pagar(self):
        if(Vagas.is_ativa==True and Vagas.is_pay==False):
            Vagas.is_pay=True
        return ('Pagamento efetuado com sucesso!')

# Veiculo registra saida, verifica se vaga está como ativa e paga, e marca vaga como não ativa

class SairVaga(UpdateView):
    model = Vagas
    http_method_names = ['post']

    def Sair(self):
        if(Vagas.is_pay==True and Vagas.is_ativa==True):
            Vagas.is_ativa(False)
        return ('Veiculo saiu')
