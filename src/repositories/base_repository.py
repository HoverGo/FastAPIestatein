from sqlalchemy import select
from src.schemas.base_schema import BaseSchema
from src.repositories.abstract_repository import AbstractRepository


class BaseRepository(AbstractRepository):
    """Базовый репозиторий, содержащий в себе базовые методы"""

    def __init__(self, db_session, model) -> None:
        self.db_session = db_session
        self.model = model
        
    async def create(self, data: BaseSchema) -> int:
        async with self.db_session() as session:
            data = data.model_dump()
            instance = self.model(**data)
            session.add(instance)
            await session.flush()
            await session.commit()
            return instance.id


    async def get_all(self) -> list[CategorySchema]:
        async with self.db_session() as session:
            query = select(self.model)
            result = await session.execute(query)
            objects = result.scalars().all()
            return objects


