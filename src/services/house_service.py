from src.services.base_service import BaseService
from src.schemas.house_schema import CategorySchemaAdd, CategorySchema, CategorySchemaOnce
from src.repositories.house_repository import CategoryRepository
from src.models.house_model import Category

class CategoryService(BaseService):

    repository = CategoryRepository
    model = Category

    async def create(self, schema: CategorySchemaAdd):
        category_id = await super().create(schema, self.repository, self.model)
        return category_id
    

    async def get_one(self, schema: CategorySchemaOnce):
        pk = schema.model_dump()["id"]
        instance = await super().get_one(self.repository, self.model, id=pk)
        return instance
    

    async def get_all(self) -> list[CategorySchema]:
        queryset = await super().get_all(self.repository, self.model)
        return queryset