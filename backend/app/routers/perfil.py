from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.db.database import get_db
from app.models.perfil import Perfil
from app.schemas.perfil import PerfilOut

router = APIRouter()

@router.get("/perfil", response_model=PerfilOut)
def obter_perfil(db: Session = Depends(get_db)):
    stmt = select(Perfil).limit(1)
    perfil = db.execute(stmt).scalar_one_or_none()
    if perfil is None:
        raise HTTPException(status_code=404, detail="Perfil não encontrado")
    return perfil