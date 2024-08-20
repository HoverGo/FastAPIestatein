from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from src.routes import router
from src.models.base_model import create_tables, delete_tables
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Асинхронный контекстный менеджер, обрабатывающий вход и выход из приложения"""
    print("App is open")
    # await delete_tables()
    # await create_tables()
    yield
    print("App is closed")


app = FastAPI(lifespan=lifespan)

app.include_router(router)

app.mount("/media", StaticFiles(directory="media"), name="media")
