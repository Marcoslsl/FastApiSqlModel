import uvicorn
from fastapi import FastAPI
from sqlmodel import SQLModel
from src.models.gem_models import *
from src.infra.configs.database import engine
from src.infra.repos.gem_repo import GemRepo
from src.api.endpoints.router import router


app = FastAPI()


app.include_router(router)


def create_db_tables():
    """Create tables."""
    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)


if __name__ == "__main__":
    create_db_tables()
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
