from src.models.base_model import BaseModel
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional


class Review(BaseModel):
    __tablename__ = "review"

    first_name: Mapped[str]
    last_name: Mapped[str]
    title: Mapped[str]
    text: Mapped[str]
    rating: Mapped[int]
    image: Mapped[Optional[str]]
    city_id: Mapped[int] = mapped_column(ForeignKey('city.id'))

    
    city: Mapped["City"] = relationship("City", back_populates="reviews", lazy="joined")


class CompanyReview(BaseModel):
    __tablename__ = "company_review"

    name: Mapped[str]
    since_year: Mapped[int]
    domain: Mapped[str]
    category_company: Mapped[str]
    text: Mapped[str]
    website_url: Mapped[str]