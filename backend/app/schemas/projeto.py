from pydantic import BaseModel
from pydantic import ConfigDict

class ProjetoBase(BaseModel):
    nome: str
    descricao: str
    url: str

class ProjetoCreate(ProjetoBase):
    pass

class ProjetoOut(ProjetoBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class ProjetoUpdate(BaseModel):
    nome: str | None = None
    descricao: str | None = None
    url: str | None = None