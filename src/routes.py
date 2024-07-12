from fastapi import APIRouter, Depends
from src.schemas.house_schema import CategorySchema, CategorySchemaAdd
from src.services.house_service import CategoryService

router = APIRouter(prefix="/api")


@router.post("/add")
async def add_category(category: CategorySchemaAdd = Depends()) -> dict:
    service = CategoryService()
    new_category_id = await service.create(category)
    return {"id": new_category_id}


@router.get("/get")
async def get_categories() -> list[CategorySchema]:
    service = CategoryService()
    categories = await service.get_all()
    return categories
