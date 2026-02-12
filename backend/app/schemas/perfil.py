from pydantic import BaseModel
from pydantic import ConfigDict

class PerfilOut(BaseModel):
    id: int
    nome: str
    bio: str | None = None
    email: str | None = None
    celular: str | None = None
    linkedin: str | None = None
    github: str | None = None
    model_config = ConfigDict(from_attributes=True)

class PerfilUpdate(BaseModel):
    nome: str | None = None
    bio: str | None = None
    email: str | None = None
    celular: str | None = None
    linkedin: str | None = None
    github: str | None = None