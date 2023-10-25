from schemas import Aluno, AlunoId
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from db import models
from pydantic import BaseModel


router = APIRouter(
    prefix="/aluno",
    tags=["Alunos"]
)


@router.get("/")
def obtener_aluno(db: Session = Depends(get_db)):
    data = db.query(models.Aluno).all()
    return data


@router.post("/")
def crear_aluno(aluno: Aluno, db: Session = Depends(get_db)):
    
    aluno_aux = aluno.dict()
    novo_aluno = models.Aluno(
        nome = aluno_aux["nome"],
        sobrenome = aluno_aux["sobrenome"],
        edade = aluno_aux["edade"],
        nota_primeiro_semestre = aluno_aux["nota_primeiro_semestre"],
        nota_segundo_semestre = aluno_aux["nota_segundo_semestre"],
        nome_professor = aluno_aux["nome_professor"],
        numero_aula = aluno_aux["numero_aula"],   
    )
    db.add(novo_aluno)
    db.commit()
    db.refresh(novo_aluno)
    return {"respuesta": "Alumno creado"}
    

@router.post("/{aluno_id}")
def obter_aluno(aluno_id: int, db: Session = Depends(get_db)):
    bus_aluno = db.query(models.Aluno).filter(models.Aluno.id == aluno_id).first()
    if not bus_aluno:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return bus_aluno

@router.put("/{aluno_id}")
def actualizar_aluno(aluno_id: int, novo_dado: Aluno, db: Session = Depends(get_db)):
    act_aluno = db.query(models.Aluno).filter(models.Aluno.id == aluno_id).first()
    if not act_aluno:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    for key, value in novo_dado.dict().items():
        setattr(act_aluno, key, value)
    db.commit()
    db.refresh(act_aluno)
    return {"respuesta": "Usuario actualizado"}

@router.delete("/")
def eliminar_aluno(aluno_id: int, db: Session = Depends(get_db)):
    bus_aluno = db.query(models.Aluno).filter(models.Aluno.id == aluno_id)
    if not bus_aluno.first():
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    bus_aluno.delete(synchronize_session=False)
    db.commit()
    return {"message": "Usuario eliminado"}

