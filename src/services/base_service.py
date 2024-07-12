from src.session import async_session
from src.schemas.base_schema import BaseSchema
from src.repositories.base_repository import BaseRepository
from src.models.base_model import BaseModel

class BaseService():
    """Сервис с базовым функционалом"""

    db_session = async_session

    async def create(self, schema: BaseSchema, Repository: BaseRepository) -> int: # Возвращает id созданного объекта
        """
        Из класса наследника передаётся схема, содержащая данные, и репозиторий,
        необходимый для использования методов взаимодействия с БД
        """
        repository = Repository(self.db_session)
        object_id = await repository.create(schema) 
        return object_id
    

    async def get_all(self, Repository: BaseRepository) -> list[BaseSchema]: # Возвращает список pydantic схем
        """Из класса наследника передаётся репозиторий, необходимый для использования методов взаимодействия с БД"""
        repository = Repository(self.db_session)
        queryset = await repository.get_all()
        return queryset