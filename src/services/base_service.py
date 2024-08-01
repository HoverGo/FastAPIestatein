from src.schemas.base_schema import BaseSchema
from src.repositories.base_repository import BaseRepository
from src.models.base_model import BaseModel

class BaseService():
    """Сервис с базовым функционалом"""

    def __init___(self, db_session) -> None:
        self.db_session = db_session

    async def create(self, data: BaseSchema, Repository: BaseRepository, model: BaseModel) -> int: # Возвращает id созданного объекта
        """
        Из класса наследника передаётся схема, содержащая данные, и репозиторий,
        необходимый для использования методов взаимодействия с БД
        """
        repository = Repository(self.db_session, model)
        object_id = await repository.create(data) 
        return object_id
    

    async def get_all(self, Repository: BaseRepository, model: BaseModel) -> list[BaseSchema]: # Возвращает список pydantic схем
        """Из класса наследника передаётся репозиторий, необходимый для использования методов взаимодействия с БД"""
        repository = Repository(self.db_session, model)
        queryset = await repository.get_all()
        return queryset