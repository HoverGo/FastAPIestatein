from sqlalchemy import select, text
from src.schemas.base_schema import BaseSchema
from src.repositories.abstract_repository import AbstractRepository
from sqlalchemy.orm import joinedload


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
            return instance

        
    async def get_one(self, **filters) -> BaseSchema:
        async with self.db_session() as session:
            query = select(self.model).filter_by(**filters)
            result = await session.execute(query)
            instance = result.scalar_one_or_none()
            return instance


    async def get_all(
            self,
            order: str = "id",
            limit: int = 100,
            offset: int = 0
            ) -> list[BaseSchema]:
        async with self.db_session() as session:
            query = select(self.model).order_by(text(order)).offset(offset).limit(limit)
            result = await session.execute(query)
            objects = result.scalars().all()
            return objects


