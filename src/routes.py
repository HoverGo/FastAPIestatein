from fastapi import APIRouter, Depends
from src.schemas.house_schema import CategorySchema, CategorySchemaAdd
from src.repositories.house_repository import CategoryRepository

router = APIRouter(prefix="/api")


@router.post("/add")
async def add_category(category: CategorySchemaAdd = Depends()) -> dict:
    new_category_id = await CategoryRepository.add_category(category)
    return {"id": new_category_id}


@router.get("/get")
async def get_categories() -> list[CategorySchema]:
    categories = await CategoryRepository.get_categories()
    return categories
