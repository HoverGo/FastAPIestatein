from fastapi import APIRouter, Depends
from src.session import async_session
from src.schemas.house_schema import CategorySchema, CategorySchemaAdd
from src.services.house_service import CategoryService
from src.schemas.house_form_schema import HouseFormSchemaAdd

router = APIRouter(prefix="/api")


@router.post("/add")
async def add_category(category: CategorySchemaAdd = Depends()) -> dict:
    session = async_session
    category_service = CategoryService(session)
    new_category_id = await category_service.create(category)
    return {"id": new_category_id}


@router.get("/get")
async def get_categories() -> list[CategorySchema]:
    session = async_session
    category_service = CategoryService(session)
    categories = await category_service.get_all()
    return categories


@router.post("/house_form")
async def add_house_form(house_form: HouseFormSchemaAdd = Depends()):
    pass
