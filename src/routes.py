from fastapi import APIRouter, Depends
from src.schemas.product_prices_schema import CategorySchema
from src.repositories.product_prices_repository import add_category_repository

router = APIRouter(prefix="/api")


@router.post("/add")
async def add_category(category: CategorySchema = Depends()) -> dict:
    new_category_id = await add_category_repository(category)
    return {"id": new_category_id}
