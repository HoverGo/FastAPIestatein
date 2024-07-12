from sqlalchemy import select
from src.models.base_model import async_session
from src.repositories.base_repository import BaseRepository
from src.models.house_model import Category
from src.schemas.house_schema import CategorySchema, CategorySchemaAdd

class CategoryRepository(BaseRepository):

    @classmethod
    async def create(cls, category: CategorySchemaAdd) -> int:
        async with async_session() as session:
            data = category.model_dump()
            new_category = Category(**data)
            session.add(new_category)
            await session.flush()
            await session.commit()
            return new_category.id


    @classmethod
    async def get_all(cls) -> list[CategorySchema]:
        async with async_session() as session:
            query = select(Category)
            result = await session.execute(query)
            category_models = result.scalars().all()
            categories = [
                CategorySchema.model_validate(category_model)
                for category_model in category_models
            ]
            return categories
