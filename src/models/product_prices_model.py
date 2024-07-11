from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.models.base_model import BaseModel


class Category(BaseModel):
    __tablename__ = "category"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

    base_products: Mapped[list["BaseProduct"]] = relationship(back_populates="category")


class BaseProduct(BaseModel):
    __tablename__ = "base_product"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    category_id: Mapped[int] = mapped_column(ForeignKey("category.id"))

    category: Mapped["Category"] = relationship(back_populates="base_products")
