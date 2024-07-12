from src.schemas.base_schema import BaseSchema
from typing import List, Optional
from pydantic import ConfigDict


class CategorySchemaAdd(BaseSchema):
    name: str


class CategorySchema(CategorySchemaAdd):
    id: int
