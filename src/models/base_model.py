from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from config.database.db_settings import DB_URL


engine = create_async_engine(DB_URL)

async_session = async_sessionmaker(engine, expire_on_commit=False)

class BaseModel(DeclarativeBase):
    pass
