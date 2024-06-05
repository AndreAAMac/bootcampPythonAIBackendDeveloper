from typing import Annotated
from pydantic import BaseModel, Field, PositiveFloat

class Atleta(BaseModel):
    nome: Annotated[str, Field(description='Nome do atleta',examples='Andre', max_length=50)]
    cpf: Annotated[str, Field(description='CPF do atleta',examples='11111111111', max_length=11)]
    idade: Annotated[int, Field(description='Idade do atleta',examples='25')]
    peso: Annotated[PositiveFloat, Field(description='Peso do atleta',examples='75.5')]
    altura: Annotated[PositiveFloat, Field(description='Altura do atleta',examples='1.75')]
    sexo: Annotated[str, Field(description='Sexo do atleta',examples='M', max_length=1)]
    