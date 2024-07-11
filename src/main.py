from fastapi import FastAPI
from src.routes import router
from src.models.base_model import create_tables, delete_tables
from src.repositories.base_repository import engine
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("App is open")
    await delete_tables()
    await create_tables()
    yield
    print("App is closed")


app = FastAPI(lifespan=lifespan)

app.include_router(router)
