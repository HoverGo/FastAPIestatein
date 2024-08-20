from fastapi import APIRouter, Depends
from src.session import async_session
from src.schemas.house_schema import IdFilter, CategorySchema, CategorySchemaAdd, CitySchemaAdd, CitySchema, PropertyTypeSchemaAdd, PropertyTypeSchema, HouseSchema, HouseSchemaOnce, HouseFormDataSchema
from src.services.house_service import CategoryService, CityService, PropertyTypeService, HouseService
from src.schemas.house_form_schema import HouseFormSchemaAdd, HouseFormSchema
from src.services.house_form_service import HouseFormService
from src.schemas.question_form_schema import QuestionFormSchema, QuestionFormSchemaAdd
from src.services.question_form_service import QuestionFormService
from src.schemas.review_schema import ReviewSchema, ReviewAddSchema, CompanyReviewSchema, CompanyReviewAddSchema
from src.services.review_service import ReviewService, CompanyReviewService

router = APIRouter(prefix="/api/v1")


# @router.post("/add_category")
# async def add_category(category: CategorySchemaAdd = Depends()) -> CategorySchema:
#     session = async_session

#     category_service = CategoryService(session)
#     new_category = await category_service.create(category)

#     return new_category


# @router.get("/categories")
# async def get_categories() -> list[CategorySchema]:
#     session = async_session

#     category_service = CategoryService(session)
#     categories = await category_service.get_all()

#     return categories


# @router.get("/category")
# async def get_category(pk: IdFilter = Depends()) -> CategorySchema:
#     session = async_session

#     category_service = CategoryService(session)
#     category = await category_service.get_one(pk)

#     return category


# @router.post("/city")
# async def add_city(city: CitySchemaAdd = Depends()) -> CitySchemaAdd:
#     session = async_session
    
#     city_service = CityService(session)
#     new_city = await city_service.create(city)

#     return new_city


# @router.get("/city")
# async def get_cities() -> list[CitySchema]:
#     session = async_session

#     city_service = CityService(session)
#     new_city = await city_service.get_all()

#     return new_city


# @router.post("/property_type")
# async def add_property_type(property_type: PropertyTypeSchemaAdd = Depends()) -> PropertyTypeSchema:
#     session = async_session

#     property_type_service = PropertyTypeService(session)
#     new_property_type = await property_type_service.create(property_type)

#     return new_property_type


# @router.get("/property_type")
# async def get_property_types() -> list[PropertyTypeSchema]:
#     session = async_session

#     property_type_service = PropertyTypeService(session)
#     property_types = await property_type_service.get_all()

#     return property_types


@router.get("/house_form_data")
async def house_form_data() -> HouseFormDataSchema:
    session = async_session

    property_type_service = PropertyTypeService(session)
    city_service = CityService(session)
    property_types = await property_type_service.get_all()
    cities = await city_service.get_all()

    data = HouseFormDataSchema(locations=cities, property_types=property_types)

    return data


@router.post("/house_form")
async def add_house_form(house_form: HouseFormSchemaAdd = Depends()) -> HouseFormSchemaAdd:
    session = async_session

    house_form_service = HouseFormService(session)
    house_form = await house_form_service.create(house_form)

    return house_form


@router.get("/house_forms")
async def get_house_forms() -> list[HouseFormSchema]:
    session = async_session

    house_form_service = HouseFormService(session)
    house_forms = await house_form_service.get_all()

    return house_forms


@router.post("/question_form")
async def add_question_form(question_form: QuestionFormSchemaAdd = Depends()) -> QuestionFormSchemaAdd:
    session = async_session

    question_form_service = QuestionFormService(session)
    new_question_form = await question_form_service.create(question_form)

    return new_question_form


# @router.get("/question_forms")
# async def get_question_forms() -> list[QuestionFormSchema]:
#     session = async_session

#     question_form_service = QuestionFormService(session)
#     question_forms = await question_form_service.get_all()

#     return question_forms


@router.post("/review")
async def add_review(review: ReviewAddSchema = Depends()) -> ReviewAddSchema:
    session = async_session
     
    review_service = ReviewService(session)
    new_review = await review_service.create(review)

    return new_review
    

@router.get("/reviews")
async def get_reviews() -> list[ReviewSchema]:
    session = async_session

    review_service = ReviewService(session)
    reviews = await review_service.get_all()

    return reviews
    

@router.post("/company_review")
async def add_company_review(company_review: CompanyReviewAddSchema = Depends()) -> CompanyReviewAddSchema:
    session = async_session

    company_review_service = CompanyReviewService(session)
    new_company_review = await company_review_service.create(company_review)

    return new_company_review


@router.get("/company_reviews")
async def get_company_review() -> list[CompanyReviewSchema]:
    session = async_session

    company_review_service = CompanyReviewService(session)
    company_reviews = await company_review_service.get_all()

    return company_reviews


@router.get("/houses")
async def get_houses() -> list[HouseSchema]:
    session = async_session
    
    house_service = HouseService(session)
    houses = await house_service.get_all()

    return houses


@router.get("/house")
async def get_house(pk: IdFilter = Depends()) -> HouseSchemaOnce:
    session = async_session
    
    house_service = HouseService(session)
    house = await house_service.get_one(pk)

    return house
