from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.models.base_model import BaseModel


class HouseForm(BaseModel):
    """Форма поиска недвижимости"""

    __tablename__ = "house_form"

    first_name: Mapped[str]
    last_name: Mapped[str]
    email: Mapped[str]
    phone: Mapped[str]
    city_id: Mapped[int] = mapped_column(ForeignKey("city.id"))
    property_type_id: Mapped[int] = mapped_column(ForeignKey("property_type.id"))
    bedrooms_count: Mapped[int]
    bathrooms_count: Mapped[int]
    budget: Mapped[int]
    prefer_email: Mapped[bool]
    prefer_phone: Mapped[bool]
    message: Mapped[str]

    city: Mapped["City"] = relationship(
        "City", back_populates="house_forms", lazy="selectin"
    )
    property_type: Mapped["PropertyType"] = relationship(
        "PropertyType", back_populates="house_forms", lazy="selectin"
    )
