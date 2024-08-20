from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.models.base_model import BaseModel
from typing import Optional


class Category(BaseModel):
    """Категории, к которым относится недвижимость"""
    __tablename__ = "category"

    name: Mapped[str] = mapped_column(unique=True)


class Tag(BaseModel):
    __tablename__ = "tag"

    name: Mapped[str]

    house_tags: Mapped[list["HouseTag"]] = relationship("HouseTag", back_populates="tag")


class HouseTag(BaseModel):
    __tablename__ = "house_tag"

    tag_id: Mapped[int] = mapped_column(ForeignKey("tag.id"))
    house_id: Mapped[int] = mapped_column(ForeignKey("house.id"))

    tag: Mapped["Tag"] = relationship("Tag", back_populates="house_tags", lazy="joined")
    house: Mapped["House"] = relationship("House", back_populates="house_tags")


class PropertyType(BaseModel):
    """Тип недвижимости"""
    __tablename__ = "property_type"

    name: Mapped[str] = mapped_column(unique=True)

    house_forms: Mapped[list["HouseForm"]] = relationship("HouseForm", back_populates="property_type")
    houses: Mapped[list["House"]] = relationship("House", back_populates="property_type")


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
    __tablename__ = "house_photo"

    photo: Mapped[str]
    house_id: Mapped[str] = mapped_column(ForeignKey("house.id"))

    house: Mapped["House"] = relationship("House", back_populates="house_photos")


class KeyFeature(BaseModel):
    __tablename__ = "key_feature"

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
    pricing_details_id: Mapped[int] = mapped_column(ForeignKey("pricing_details.id"))

    pricing_details: Mapped["PricingDetails"] = relationship("PricingDetails", back_populates="additional_fee")


class MonthlyCost(BaseModel):
    __tablename__ = "monthly_cost"

    property_taxes: Mapped[int]
    homeowners_association_fee: Mapped[int]
    pricing_details_id: Mapped[int] = mapped_column(ForeignKey("pricing_details.id"))

    pricing_details: Mapped["PricingDetails"] = relationship("PricingDetails", back_populates="monthly_cost")


class TotalInitialCost(BaseModel):
    __tablename__ = "total_initial_cost"

    listing_price: Mapped[int]
    additional_fees: Mapped[int]
    down_payment: Mapped[int]
    down_payment_percent: Mapped[int]
    mortgage_amount: Mapped[int]
    pricing_details_id: Mapped[int] = mapped_column(ForeignKey("pricing_details.id"))
    
    pricing_details: Mapped["PricingDetails"] = relationship("PricingDetails", back_populates="total_initial_cost")


class MonthlyExpense(BaseModel):
    __tablename__ = "monthly_expense"

    property_taxes: Mapped[int]
    homeowners_association_fee: Mapped[int]
    mortgage_payment: Mapped[int]
    property_insurance: Mapped[int]
    pricing_details_id: Mapped[int] = mapped_column(ForeignKey("pricing_details.id"))
    

    pricing_details: Mapped["PricingDetails"] = relationship("PricingDetails", back_populates="monthly_expense")


class PricingDetails(BaseModel):
    __tablename__ = "pricing_details"

    house_id: Mapped[int] = mapped_column(ForeignKey("house.id"))
    listing_price: Mapped[int]
    # additional_fee_id: Mapped[Optional[int]] = mapped_column(ForeignKey("additional_fee.id"))
    # monthly_cost_id: Mapped[Optional[int]] = mapped_column(ForeignKey("monthly_cost.id"))
    # total_initial_cost_id: Mapped[Optional[int]] = mapped_column(ForeignKey("total_initial_cost.id"))
    # monthly_expense_id: Mapped[Optional[int]] = mapped_column(ForeignKey("monthly_expense.id"))

    additional_fee: Mapped["AdditionalFee"] = relationship("AdditionalFee", back_populates="pricing_details", lazy="joined")
    monthly_cost: Mapped["MonthlyCost"] = relationship("MonthlyCost", back_populates="pricing_details", lazy="joined")
    total_initial_cost: Mapped["TotalInitialCost"] = relationship("TotalInitialCost", back_populates="pricing_details", lazy="joined")
    monthly_expense: Mapped["MonthlyExpense"] = relationship("MonthlyExpense", back_populates="pricing_details", lazy="joined")
    house: Mapped["House"] = relationship("House", back_populates="pricing_details")


class House(BaseModel):
    __tablename__ = "house"

    name: Mapped[str]
    city_id: Mapped[int] = mapped_column(ForeignKey("city.id"))
    property_type_id: Mapped[int] = mapped_column(ForeignKey("property_type.id"))
    price: Mapped[int]
    title: Mapped[str]
    description: Mapped[str]
    bedrooms_count: Mapped[int]
    bathrooms_count: Mapped[int]
    area: Mapped[int]

    key_features: Mapped[list["KeyFeature"]] = relationship("KeyFeature", back_populates="house", lazy="selectin")
    house_photos: Mapped[list["HousePhoto"]] = relationship("HousePhoto", back_populates="house", lazy="selectin")
    house_tags: Mapped[list["HouseTag"]] = relationship("HouseTag", back_populates="house", lazy="selectin")
    property_type: Mapped["PropertyType"] = relationship("PropertyType", back_populates="houses", lazy="joined")
    city: Mapped["City"] = relationship("City", back_populates="houses", lazy="joined")
    pricing_details: Mapped["PricingDetails"] = relationship("PricingDetails", back_populates="house", lazy="joined")







    

    





