from src.repositories.base_repository import BaseRepository
from src.models.house_model import Category
from src.schemas.house_schema import CategorySchema, CategorySchemaAdd

class CategoryRepository(BaseRepository):

    async def create(self, category_data: CategorySchemaAdd) -> int:
        id = await super().create(category_data)
        return id


    async def get_all(self) -> list[CategorySchema]:
        category_models = await super().get_all()
        categories = [
            CategorySchema.model_validate(category_model)
            for category_model in category_models
        ]
        return categories
