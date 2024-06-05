from typing import Annotated

from pydantic import Field
from bootcampPythonAIBackendDeveloper.ApiFlask.pythonProject.workout_api.contrib.schemas import BaseSchema


class CentroTreinamento(BaseSchema):
    nome: Annotated[str, Field(description='Nome do centro de treinamento',example='CT', max_length=20)]
    endereco: Annotated[str, Field(description='Endereço do centro de treinamento',example='Rua A, 001', max_length=60)]
    proprietario: Annotated[str, Field(description='Proprietario do centro de treinamento',example='Carlos', max_length=30)]