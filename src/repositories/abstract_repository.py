from sqlalchemy import select
from abc import abstractmethod
from src.schemas.base_schema import BaseSchema


class AbstractRepository():
    """Базовый репозиторий, содержащий в себе базовые абстрактные методы"""
    
    @abstractmethod
    async def create():
        pass

    @abstractmethod
    async def get_all():
        pass