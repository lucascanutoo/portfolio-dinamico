from fastapi import FastAPI
from app.db.database import engine, Base
from app.routers.projetos import router

app = FastAPI()

Base.metadata.create_all(bind=engine)
app.include_router(router, prefix="/api")

@app.get("/")
def read_root():
    return {"Hello": "World"}