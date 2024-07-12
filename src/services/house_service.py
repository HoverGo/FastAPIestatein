from src.services.base_service import BaseService
from src.schemas.house_schema import CategorySchemaAdd, CategorySchema
from src.repositories.house_repository import CategoryRepository

class CategoryService(BaseService):

    @classmethod
    async def create(cls, schema: CategorySchemaAdd):
        object_id = await super().create(schema, CategoryRepository)
        return object_id
    

    @classmethod
    async def get_all(cls) -> list[CategorySchema]:
        queryset = await super().get_all(CategoryRepository)
        return queryset