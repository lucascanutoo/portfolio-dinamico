from fastapi import APIRouter, Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.db.database import get_db
from app.models.projeto import Projeto
from app.schemas.projeto import ProjetoOut
from app.schemas.projeto import ProjetoCreate
from app.schemas.projeto import ProjetoUpdate

router = APIRouter()

@router.get("/projetos", response_model=list[ProjetoOut])
def listar(db: Session = Depends(get_db)):
    result = db.execute(select(Projeto))
    projetos = result.scalars().all()
    return projetos

@router.post("/projetos", response_model=ProjetoOut)
def criar_projeto(projeto: ProjetoCreate, db: Session = Depends(get_db)):
    novo_projeto = Projeto(
        nome=projeto.nome,
        descricao=projeto.descricao,
        url=projeto.url
    )
    db.add(novo_projeto)
    db.commit()
    db.refresh(novo_projeto)
    return novo_projeto

@router.get("/projetos/{projeto_id}", response_model=ProjetoOut)
def obter_projeto(projeto_id: int, db: Session = Depends(get_db)):
    projeto = db.get(Projeto, projeto_id)
    if projeto is None:
        raise HTTPException(status_code=404, detail="Projeto não encontrado")
    return projeto

@router.delete("/projetos/{projeto_id}")
def deletar_projeto(projeto_id: int, db: Session = Depends(get_db)):
    projeto = db.get(Projeto, projeto_id)
    if projeto is None:
        raise HTTPException(status_code=404, detail="Projeto não encontrado")
    db.delete(projeto)
    db.commit()
    return {"detail": "Projeto deletado com sucesso"}

@router.put("/projetos/{projeto_id}", response_model=ProjetoOut)
def atualizar_projeto(projeto_id: int, projeto_atualizado: ProjetoUpdate, db: Session = Depends(get_db)):
    projeto = db.get(Projeto, projeto_id)
    if projeto is None:
        raise HTTPException(status_code=404, detail="Projeto não encontrado")
    
    dados = projeto_atualizado.model_dump(exclude_unset=True)
    for chave, valor in dados.items():
        setattr(projeto, chave, valor)

    db.commit()
    db.refresh(projeto)
    return projeto