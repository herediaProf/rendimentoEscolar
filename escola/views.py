from rest_framework import viewsets
from .models import Aluno, MetricaDesempenho
from .serializers import AlunoSerializer, MetricaDesempenhoSerializer


class AlunoViewSet(viewsets.ModelViewSet):
    """
    Esta ViewSet cria automaticamente as rotas de listagem (GET),
    criação (POST), atualização (PUT/PATCH) e exclusão (DELETE) para Alunos.
    """

    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


class MetricaDesempenhoViewSet(viewsets.ModelViewSet):
    queryset = MetricaDesempenho.objects.all()
    serializer_class = MetricaDesempenhoSerializer
