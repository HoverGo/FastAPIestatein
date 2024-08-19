from src.schemas.base_schema import BaseSchema
from src.repositories.base_repository import BaseRepository
from src.models.base_model import BaseModel

class BaseService():
    """Сервис с базовым функционалом"""

    def __init__(self, db_session) -> None:
        self.db_session = db_session

    async def create(self, data: BaseSchema, Repository: BaseRepository, model: BaseModel) -> BaseSchema: # Возвращает созданный объект
        """
        Из класса наследника передаются схема, содержащая данные, и репозиторий,
        необходимый для использования методов взаимодействия с БД
        """
        repository = Repository(self.db_session, model)
        instance = await repository.create(data) 
        return instance
    

    async def get_one(self, Repository: BaseRepository, model: BaseModel, **filters):
        """
        Из класса наследника передаются модель, репозиторий и фильтры,
        по которым через репозиторий получается один объект
        """
        repository = Repository(self.db_session, model)
        instance = await repository.get_one(**filters)
        return instance
    

    async def get_all(self, Repository: BaseRepository, model: BaseModel) -> list[BaseSchema]: # Возвращает список pydantic схем
        """Из класса наследника передаётся репозиторий, необходимый для использования методов взаимодействия с БД"""
        repository = Repository(self.db_session, model)
        queryset = await repository.get_all()
        return queryset