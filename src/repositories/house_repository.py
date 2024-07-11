from sqlalchemy import select
from src.repositories.base_repository import async_session
from src.models.house_model import CategoryModel
from src.schemas.house_schema import CategorySchema

class CategoryRepository:

    @classmethod
    async def add_category(cls, category: CategorySchema) -> int:
        async with async_session() as session:
            data = category.model_dump()
            new_category = CategoryModel(**data)
            session.add(new_category)
            await session.flush()
            await session.commit()
            return new_category.id
        
    @classmethod
    async def get_categories(cls) -> list[CategorySchema]:
        async with async_session() as session:
            query = select(CategoryModel)
            result = await session.execute(query)
            category_models = result.scalar().all()
            categories = [CategorySchema.model_validate(category_model) for category_model in category_models]
            return categories
