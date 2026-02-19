from fastapi import FastAPI
from app.db.database import engine, Base
from app.routers.projetos import router
<<<<<<< HEAD
from app.routers import projetos, perfil
=======
from app import models
>>>>>>> 1088c6865ef90686e98ceadf13736865afc6f362

app = FastAPI()

Base.metadata.create_all(bind=engine)
app.include_router(router, prefix="/api")
app.include_router(projetos.router, prefix="/api")
app.include_router(perfil.router, prefix="/api")

@app.get("/")
def read_root():
    return {"Hello": "World"}