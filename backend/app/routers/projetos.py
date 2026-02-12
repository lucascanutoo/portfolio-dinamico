from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.db.database import get_db
from app.models.projeto import Projeto
from app.schemas.projeto import ProjetoOut

router = APIRouter()

@router.get("/projetos", response_model=list[ProjetoOut])
def listar(db: Session = Depends(get_db)):
    result = db.execute(select(Projeto))
    projetos = result.scalars().all()
    return projetos