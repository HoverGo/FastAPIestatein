from sqlalchemy import select
from src.repositories.base_repository import BaseRepository
from src.models.house_model import Category
from src.schemas.house_schema import CategorySchema, CategorySchemaAdd

class CategoryRepository(BaseRepository):

    def __init__(self, db_session):
        self.db_session = db_session

    
    async def create(self, category: CategorySchemaAdd) -> int:
        async with self.db_session() as session:
            data = category.model_dump()
            new_category = Category(**data)
            session.add(new_category)
            await session.flush()
            await session.commit()
            return new_category.id


    async def get_all(self) -> list[CategorySchema]:
        async with self.db_session() as session:
            query = select(Category)
            result = await session.execute(query)
            category_models = result.scalars().all()
            categories = [
                CategorySchema.model_validate(category_model)
                for category_model in category_models
            ]
            return categories
