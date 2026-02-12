from app.db.database import Base
from sqlalchemy import Column, Integer, String

class Perfil(Base):
    __tablename__ = "perfis"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True, nullable=False)
    bio = Column(String, nullable=True)
    email = Column(String, nullable=True)
    celular = Column(String, nullable=True)
    linkedin = Column(String, nullable=True)
    github = Column(String, nullable=True)