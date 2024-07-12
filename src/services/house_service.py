from src.services.base_service import BaseService
from src.schemas.house_schema import CategorySchemaAdd, CategorySchema
from src.repositories.house_repository import CategoryRepository

class CategoryService(BaseService):

    repository = CategoryRepository

    async def create(self, schema: CategorySchemaAdd):
        category_id = await super().create(schema, self.repository)
        return category_id
    

    async def get_all(self) -> list[CategorySchema]:
        queryset = await super().get_all(self.repository)
        return queryset