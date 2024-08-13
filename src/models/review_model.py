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