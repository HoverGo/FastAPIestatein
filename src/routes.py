from fastapi import APIRouter, Depends
from src.session import async_session
from src.schemas.house_schema import CategorySchema, CategorySchemaAdd, CategorySchemaOnce, CitySchemaAdd, CitySchema, PropertyTypeSchemaAdd, PropertyTypeSchema
from src.services.house_service import CategoryService, CityService, PropertyTypeService
from src.schemas.house_form_schema import HouseFormSchemaAdd, HouseFormSchema
from src.services.house_form_service import HouseFormService, HouseFormDataService


router = APIRouter(prefix="/api/v1")


@router.post("/add_category")
async def add_category(category: CategorySchemaAdd = Depends()) -> CategorySchema:
    session = async_session
    category_service = CategoryService(session)
    new_category = await category_service.create(category)
    return new_category


@router.get("/categories")
async def get_categories() -> list[CategorySchema]:
    session = async_session
    category_service = CategoryService(session)
    categories = await category_service.get_all()
    return categories


@router.get("/category")
async def get_category(category_pk: CategorySchemaOnce = Depends()) -> CategorySchema:
    session = async_session
    category_service = CategoryService(session)
    category = await category_service.get_one(category_pk)
    return category


@router.post("/city")
async def add_city(city: CitySchemaAdd = Depends()) -> CitySchemaAdd:
    session = async_session
    city_service = CityService(session)
    new_city = await city_service.create(city)
    return new_city


@router.post("/property_type")
async def add_property_type(property_type: PropertyTypeSchemaAdd = Depends()) -> PropertyTypeSchema:
    session = async_session
    property_type_service = PropertyTypeService(session)
    new_property_type = await property_type_service.create(property_type)
    return new_property_type


@router.get("/house_form_data")
async def house_form_data() -> dict:
    session = async_session
    house_form_data_service = HouseFormDataService(session)
    data = {
        "data": house_form_data_service.get_all()
        }
    return data


@router.post("/house_form")
async def add_house_form(house_form: HouseFormSchemaAdd = Depends()) -> HouseFormSchemaAdd:
    session = async_session
    house_form_service = HouseFormService(session)
    house_form = await house_form_service.create(house_form)
    return house_form


@router.get("/house_forms")
async def get_house_forms() -> list[HouseFormSchemaAdd]:
    session = async_session
    house_form_service = HouseFormService(session)
    house_forms = await house_form_service.get_all()
    return house_forms
