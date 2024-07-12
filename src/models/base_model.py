from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from src.session import engine



class BaseModel(DeclarativeBase):
    __abstract__ = True
    
    id: Mapped[int] = mapped_column(primary_key=True)


# Создание всех таблиц, наследующихся от BaseModel
async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(BaseModel.metadata.create_all)


# Удаление всех таблиц, наследующихся от BaseModel
async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(BaseModel.metadata.drop_all)


