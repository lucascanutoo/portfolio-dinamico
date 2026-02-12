from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.db.database import get_db
from app.models.perfil import Perfil
from app.schemas.perfil import PerfilOut
from app.schemas.perfil import PerfilUpdate

router = APIRouter()

@router.get("/perfil", response_model=PerfilOut)
def obter_perfil(db: Session = Depends(get_db)):
    stmt = select(Perfil).limit(1)
    perfil = db.execute(stmt).scalar_one_or_none()
    if perfil is None:
        raise HTTPException(status_code=404, detail="Perfil não encontrado")
    return perfil

@router.put("/perfil", response_model=PerfilOut)
def atualizar_perfil(perfil_atualizado: PerfilUpdate, db: Session = Depends(get_db)):
    stmt = select(Perfil).limit(1)
    perfil = db.execute(stmt).scalar_one_or_none()
    if perfil is None:
        dados = perfil_atualizado.model_dump(exclude_unset=True)
        if 'nome' not in dados or dados['nome'] is None:
            raise HTTPException(status_code=400, detail="O campo 'nome' é obrigatório para criar um perfil")
        novo_perfil = Perfil(**dados)
        db.add(novo_perfil)
        db.commit()
        db.refresh(novo_perfil)
        return novo_perfil
    else:
        dados = perfil_atualizado.model_dump(exclude_unset=True)
        for chave, valor in dados.items():
            setattr(perfil, chave, valor)

        db.commit()
        db.refresh(perfil)
        return perfil