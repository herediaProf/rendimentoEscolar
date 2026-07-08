# alunos/views.py
from django.shortcuts import render, get_object_or_404
from escola.models import Aluno
from .services import obter_analise_profunda_aluno

# Adicione ao final de alunos/views.py
from .services import obter_top_10_alunos, obter_piores_10_alunos


def diagnostico_individual(request, aluno_id):
    aluno = get_object_or_404(Aluno, id=aluno_id)

    # Executa a query de alta performance do PostgreSQL
    boletim_analitico = obter_analise_profunda_aluno(aluno_id)

    # Motor de Tomada de Decisão Pedagógica (Geração de Alertas)
    alertas_intervencao = []
    for item in boletim_analitico:
        # Alerta de Nota abaixo da Média da Sala
        if (
            item["nota_aluno"]
            and item["nota_aluno"] < 6.0
            and item["nota_aluno"] < item["media_turma"]
        ):
            alertas_intervencao.append(
                {
                    "disciplina": item["disciplina"],
                    "bimestre": item["bimestre"],
                    "motivo": f"Nota ({item['nota_aluno']}) abaixo da média da turma ({item['media_turma']}). Posição atual: {item['ranking_posicao']}º no ranking.",
                    "grau_risco": "🔴 Crítico (Defasagem)",
                }
            )

        # Alerta de Absenteísmo (Risco por Faltas)
        if item["faltas"] > 10:
            alertas_intervencao.append(
                {
                    "disciplina": item["disciplina"],
                    "bimestre": item["bimestre"],
                    "motivo": f"O estudante acumula {item['faltas']} faltas neste componente curricular.",
                    "grau_risco": "🟡 Atenção (Frequência)",
                }
            )

    context = {
        "aluno": aluno,
        "boletim_analitico": boletim_analitico,
        "alertas_intervencao": alertas_intervencao,
    }
    return render(request, "alunos/diagnostico.html", context)


def painel_extremos_turma(request):
    top_10 = obter_top_10_alunos()
    piores_10 = obter_piores_10_alunos()

    context = {
        "top_10": top_10,
        "piores_10": piores_10,
    }
    return render(request, "alunos/extremos.html", context)
