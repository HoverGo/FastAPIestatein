from src.schemas.base_schema import BaseSchema, BaseSchemaWithPhone
from src.schemas.house_schema import CitySchema, PropertyTypeSchema
from pydantic import EmailStr, Field


class HouseFormSchemaAdd(BaseSchemaWithPhone):
    first_name: str
    last_name: str
    email: EmailStr
    city_id: int
    property_type_id: int
    bedrooms_count: int = Field(gt=1, le=99)
    bathrooms_count: int = Field(gt=1, le=99)
    budget: int
    prefer_email: bool
    prefer_phone: bool
    message: str


class HouseFormSchema(HouseFormSchemaAdd):
    id: int
    city: CitySchema
    property_type: PropertyTypeSchema
