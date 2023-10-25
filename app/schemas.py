from pydantic import BaseModel


class Aluno(BaseModel):
    
    nome: str
    sobrenome: str
    edade: int
    nota_primeiro_semestre: float
    nota_segundo_semestre: float
    nome_professor: str
    numero_aula: int

class AlunoId(BaseModel):
    id: int