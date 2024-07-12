from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.models.base_model import BaseModel
# from src.models.house_form_model import HouseForm

class Category(BaseModel):
    """Категории, к которым относится недвижимость"""
    __tablename__ = "category"

    name: Mapped[str] = mapped_column(unique=True)


class PropertyType(BaseModel):
    """Тип недвижимости"""
    __tablename__ = "property_type"

    name: Mapped[str] = mapped_column(unique=True)

    # house_forms: Mapped[list["HouseForm"]] = relationship(back_populates="property_type")


class Country(BaseModel):
    __tablename__ = "country"

    name: Mapped[str] = mapped_column(unique=True)

    cities: Mapped[list["City"]] = relationship(back_populates="country")


class City(BaseModel):
    __tablename__ = "city"

    name: Mapped[str]
    country_id: Mapped[int] = mapped_column(ForeignKey("country.id"))

    country: Mapped["Country"] = relationship(back_populates="cities")
    # house_forms: Mapped["HouseForm"] = relationship(back_populates="city")