from src.schemas.base_schema import BaseSchema
from typing import List, Optional


class CategorySchema(BaseSchema):
    name: str


class BaseProductSchema(BaseSchema):
    name: str
    category_id: List[CategorySchema]
