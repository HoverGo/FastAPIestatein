from src.schemas.base_schema import BaseSchema
from src.schemas.house_schema import CitySchema, PropetryTypeSchema
from pydantic import EMailStr, Field

class HouseFormSchemaAdd(BaseSchema):
    first_name: str
    last_name: str
    email: EMailStr
    phone: str
    city: CitySchema
    property_type: PropetryTypeSchema
    bedrooms_count: int
    bathrooms_count: int
    budget: int
    prefer_email: bool
    prefer_phone: bool
    message: str


class HouseFormSchema(HouseFormSchemaAdd):
    id: int
    city_id: int
    property_type_id: int
