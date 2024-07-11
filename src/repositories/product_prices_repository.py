from src.repositories.base_repository import async_session
from src.models.product_prices_model import Category
from src.schemas.product_prices_schema import CategorySchema


async def add_category_repository(category: CategorySchema) -> int:
    async with async_session() as session:
        data = category.model_dump()
        new_category = Category(**data)
        session.add(new_category)
        await session.flush()
        await session.commit()
        return new_category.id
