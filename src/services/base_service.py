from src.schemas.base_schema import BaseSchema
from src.repositories.base_repository import BaseRepository
from src.models.base_model import BaseModel

class BaseService():
    
    @classmethod
    async def create(cls, schema: BaseSchema, repository: BaseRepository) -> int:
        object_id = await repository.create(schema) 
        return object_id
    

    @classmethod
    async def get_all(cls, repository: BaseRepository) -> list[BaseSchema]:
        queryset = await repository.get_all()
        return queryset