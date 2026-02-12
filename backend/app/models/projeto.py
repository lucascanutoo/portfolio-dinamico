from app.db.database import Base
from sqlalchemy import Column, Integer, String

class Projeto(Base):
    __tablename__ = "projetos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True, nullable=False)
    descricao = Column(String, nullable=False)
    url = Column(String, nullable=False)