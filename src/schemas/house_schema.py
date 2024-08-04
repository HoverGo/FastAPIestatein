from src.schemas.base_schema import BaseSchema
from typing import List, Optional


class CategorySchemaAdd(BaseSchema):
    name: str


class CategorySchema(CategorySchemaAdd):
    id: int


class CategorySchemaOnce(BaseSchema):
    id: int


class PropertyTypeSchemaAdd(BaseSchema):
    name: str


class PropetryTypeSchema(PropertyTypeSchemaAdd):
    id: int


class CountrySchemaAdd(BaseSchema):
    name: str


class CountrySchema(CountrySchemaAdd):
    id: int


class CitySchemaAdd(BaseSchema):
    name: str
    country: CountrySchema


class CitySchema(CitySchemaAdd):
    id: int
    country_id: int
