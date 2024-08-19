from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.models.base_model import BaseModel
from typing import Optional


class Category(BaseModel):
    """Категории, к которым относится недвижимость"""
    __tablename__ = "category"

    name: Mapped[str] = mapped_column(unique=True)

    houses: Mapped[list["House"]] = relationship("House", back_populates="categories")


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
    house_forms: Mapped[list["HouseForm"]] = relationship("HouseForm", back_populates="city")
    reviews: Mapped[list["Review"]] = relationship("Review", back_populates="city")
    houses: Mapped[list["House"]] = relationship("House", back_populates="city")


class HousePhoto(BaseModel):
    __tablename__ = "house_photos"

    photo: Mapped[str]
    house_id: Mapped[str] = mapped_column(ForeignKey("house.id"))

    house: Mapped["House"] = relationship("House", back_populates="house_photos")


class KeyFeature(BaseModel):
    __tablename__ = "key_features"

    name: Mapped[str]
    house_id: Mapped[str] = mapped_column(ForeignKey("house.id"))

    house: Mapped["House"] = relationship("House", back_populates="key_features")


class AdditionalFee(BaseModel):
    __tablename__ = "additional_fee"

    property_transfer_tax: Mapped[int]
    legal_fees: Mapped[int]
    home_inspection: Mapped[int]
    property_insurance: Mapped[int]
    mortgage_fees: Mapped[str]

    pricing_details: Mapped["PricingDetails"] = relationship("PricingDetails", back_populates="additional_fees")


class MonthlyCost(BaseModel):
    __tablename__ = "monthly_cost"

    property_taxes: Mapped[int]
    homeowners_association_fee: Mapped[int]

    pricing_details: Mapped["PricingDetails"] = relationship("PricingDetails", back_populates="monthly_cost")


class TotalInitialCost(BaseModel):
    __tablename__ = "total_initial_cost"

    listing_price: Mapped[int]
    additional_fees: Mapped[int]
    down_payment: Mapped[int]
    down_payment_percent: Mapped[int]
    mortgage_amount: Mapped[int]
    
    pricing_details: Mapped["PricingDetails"] = relationship("PricingDetails", back_populates="total_initial_cost")


class MonthlyExpense(BaseModel):
    __tablename__ = "monthly_expense"

    property_taxes: Mapped[int]
    homeowners_association_fee: Mapped[int]
    mortgage_payment: Mapped[int]
    property_insurance: Mapped[int]

    pricing_details: Mapped["PricingDetails"] = relationship("PricingDetails", back_populates="monthly_expense")


class PricingDetails(BaseModel):
    __tablename__ = "pricing_details"

    house_id: Mapped[int] = mapped_column(ForeignKey("house.id"))
    listing_price: Mapped[int]
    additional_fee_id: Mapped[Optional[int]] = mapped_column(ForeignKey("additional_fee.id"))
    monthly_cost_id: Mapped[Optional[int]] = mapped_column(ForeignKey("monthly_cost.id"))
    total_initial_cost_id: Mapped[Optional[int]] = mapped_column(ForeignKey("total_initial_cost.id"))
    monthly_expense_id: Mapped[Optional[int]] = mapped_column(ForeignKey("monthly_expense.id"))

    additional_fee: Mapped["AdditionalFee"] = relationship("AdditionalFee", back_populates="pricing_details", lazy="joined")
    monthly_cost: Mapped["MonthlyCost"] = relationship("MonthlyCost", back_populates="pricing_details", lazy="joined")
    total_initial_cost: Mapped["TotalInitialCost"] = relationship("TotalInitialCost", back_populates="pricing_details", lazy="joined")
    monthly_expense: Mapped["MonthlyExpense"] = relationship("MonthlyExpense", back_populates="pricing_details", lazy="joined")


class House(BaseModel):
    __tablename__ = "house"

    name: Mapped[str]
    city_id: Mapped[int] = mapped_column(ForeignKey("city.id"))
    category_id: Mapped[int] = mapped_column(ForeignKey("category.id"))
    price: Mapped[int]
    description: Mapped[str]
    bedrooms_count: Mapped[int]
    bathrooms_count: Mapped[int]
    area: Mapped[int]

    category: Mapped["Category"] = relationship("Category", back_populates="houses", lazy="joined")
    city: Mapped["City"] = relationship("City", back_populates="houses", lazy="joined")
    pricing_details: Mapped["PricingDetails"] = relationship("PricingDetails", back_populates="house", lazy="joined")







    

    





