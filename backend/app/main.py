from fastapi import FastAPI
from app.db.database import engine, Base
from app.routers.projetos import router as projetos_router
from app.routers.perfil import router as perfil_router
from app.auth.router import router as auth_router
from app import models

app = FastAPI()

Base.metadata.create_all(bind=engine)
app.include_router(projetos_router, prefix="/api")
app.include_router(perfil_router, prefix="/api")
app.include_router(auth_router, prefix="/api")

@app.get("/")
def read_root():
    return {"Hello": "World"}