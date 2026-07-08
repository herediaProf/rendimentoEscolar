# alunos/urls.py
from django.urls import path
from . import views

app_name = "alunos"

urlpatterns = [
    # Rota: http://127.0.0.1:8000/alunos/extremos/
    path("extremos/", views.painel_extremos_turma, name="painel_extremos"),
    # Rota: http://127.0.0.1:8000/alunos/diagnostico/4/
    path(
        "diagnostico/<int:aluno_id>/",
        views.diagnostico_individual,
        name="diagnostico_individual",
    ),
]
