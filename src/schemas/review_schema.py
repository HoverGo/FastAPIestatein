from src.schemas.base_schema import BaseSchema
from src.schemas.house_schema import CitySchema
from typing import Optional
from pydantic import Field


class ReviewAddSchema(BaseSchema):
    first_name: str
    last_name: str
    title: str
    text: str
    rating: int = Field(gt=0, le=5)
    image: Optional[str] = None
    city_id: int


class ReviewSchema(ReviewAddSchema):
    id: int
    city: CitySchema


class CompanyReviewAddSchema(BaseSchema):
    name: str
    since_year: int
    domain: str
    category_company: str
    text: str
    website_url: str


class CompanyReviewSchema(CompanyReviewAddSchema):
    id: int
