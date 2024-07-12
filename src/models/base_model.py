from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from config.database.db_settings import DB_URL



class BaseModel(DeclarativeBase):
    __abstract__ = True
    
    id: Mapped[int] = mapped_column(primary_key=True)


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(BaseModel.metadata.create_all)


async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(BaseModel.metadata.drop_all)

engine = create_async_engine(DB_URL)

async_session = async_sessionmaker(engine, expire_on_commit=False)
