from rest_framework import serializers
from .models import Aluno, MetricaDesempenho


class AlunoSerializer(serializers.ModelSerializer):
    # Campo calculado dinamicamente que criamos no models.py
    class Meta:
        model = Aluno
        fields = ["id", "nome", "email", "matricula", "criado_em"]


class MetricaDesempenhoSerializer(serializers.ModelSerializer):
    # Traz o status de aprovação calculado pela nossa regra de negócio @property
    aprovado = serializers.ReadOnlyField()

    class Meta:
        model = MetricaDesempenho
        fields = [
            "id",
            "aluno",
            "disciplina",
            "nota",
            "frequencia_porcentagem",
            "data_avaliacao",
            "aprovado",
        ]
