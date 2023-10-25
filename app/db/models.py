from db.database import Base
from sqlalchemy import Column, Integer, String, Float, Boolean

class Aluno(Base):
    __tablename__="aluno"
    id = Column(Integer, primary_key=True, autoincrement= True)
    nome = Column(String)
    sobrenome = Column(String)
    edade = Column(Integer)
    nota_primeiro_semestre = Column(Float)
    nota_segundo_semestre = Column(Float)
    nome_professor = Column(String)
    numero_aula = Column(Integer)