from fastapi import APIRouter, Depends
from src.session import async_session
from src.schemas.house_schema import CategorySchema, CategorySchemaAdd, CategorySchemaOnce
from src.services.house_service import CategoryService
from src.schemas.house_form_schema import HouseFormSchemaAdd, HouseFormSchema
from src.services.house_form_service import HouseFormService

router = APIRouter(prefix="/api")


@router.post("/add_category")
async def add_category(category: CategorySchemaAdd = Depends()) -> dict:
    session = async_session
    category_service = CategoryService(session)
    new_category_id = await category_service.create(category)
    return {"id": new_category_id}


@router.get("/get_categories")
async def get_categories() -> list[CategorySchema]:
    session = async_session
    category_service = CategoryService(session)
    categories = await category_service.get_all()
    return categories


@router.get("/get_category")
async def get_category(category_pk: CategorySchemaOnce = Depends()) -> CategorySchema:
    session = async_session
    category_service = CategoryService(session)
    category = await category_service.get_one(category_pk)
    return category


@router.post("/house_form")
async def add_house_form(house_form: HouseFormSchemaAdd = Depends()):
    pass

@router.get("/get_house_form")
async def get_house_forms() -> list[HouseFormSchemaAdd]:
    session = async_session
    house_form_service = HouseFormService(session)
    house_forms = await house_form_service.get_all()
    return house_forms
