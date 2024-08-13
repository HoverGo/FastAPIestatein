from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.models.base_model import BaseModel

class Category(BaseModel):
    """Категории, к которым относится недвижимость"""
    __tablename__ = "category"

    name: Mapped[str] = mapped_column(unique=True)


class PropertyType(BaseModel):
    """Тип недвижимости"""
    __tablename__ = "property_type"

    name: Mapped[str] = mapped_column(unique=True)

    house_forms: Mapped[list["HouseForm"]] = relationship("HouseForm", back_populates="property_type")


class Country(BaseModel):
    __tablename__ = "country"

    name: Mapped[str] = mapped_column(unique=True)

    cities: Mapped[list["City"]] = relationship("City", back_populates="country")


class City(BaseModel):
    __tablename__ = "city"

    name: Mapped[str]
    country_id: Mapped[int] = mapped_column(ForeignKey("country.id"))

    country: Mapped["Country"] = relationship("Country", back_populates="cities", lazy="joined")
    house_forms: Mapped["HouseForm"] = relationship("HouseForm", back_populates="city")
    reviews: Mapped["Review"] = relationship("Review", back_populates="city")