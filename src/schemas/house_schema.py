from src.schemas.base_schema import BaseSchema, BaseSchemaWithPhone
from typing import List, Optional
from pydantic import EmailStr, Field


class IdFilter(BaseSchema):
    id: int


class CategorySchemaAdd(BaseSchema):
    name: str


class CategorySchema(CategorySchemaAdd):
    id: int


class TagSchema(BaseSchema):
    id: int
    name: str


class HouseTagSchema(BaseSchema):
    id: int
    tag: TagSchema


class PropertyTypeSchemaAdd(BaseSchema):
    name: str


class PropertyTypeSchema(PropertyTypeSchemaAdd):
    id: int


class CountrySchemaAdd(BaseSchema):
    name: str


class CountrySchema(CountrySchemaAdd):
    id: int


class CitySchemaAdd(BaseSchema):
    name: str
    country_id: int


class CitySchema(CitySchemaAdd):
    id: int
    country: CountrySchema


class HouseFormDataSchema(BaseSchema):
    locations: list[CitySchema]
    property_types: list[PropertyTypeSchema]


class HousePhotoSchema(BaseSchema):
    id: int
    photo: str


class KeyFeaturesSchema(BaseSchema):
    id: int
    name: str


class AdditionalFeeSchema(BaseSchema):
    id: int
    property_transfer_tax: int
    legal_fees: int
    home_inspection: int
    property_insurance: int
    mortgage_fees: str


class MonthlyCostSchema(BaseSchema):
    id: int
    property_taxes: int
    homeowners_association_fee: int


class TotalInitialCostSchema(BaseSchema):
    id: int
    listing_price: int
    additional_fees: int
    down_payment: int
    down_payment_percent: int
    mortgage_amount: int


class MonthlyExpenseSchema(BaseSchema):
    id: int
    proprety_taxes: int
    homeowners_association_fee: int
    mortgage_payment: int
    property_insurance: int


class PricingDetailsSchema(BaseSchema):
    id: int
    listing_price: int
    additional_fee: Optional[AdditionalFeeSchema] = None
    monthly_cost: Optional[MonthlyCostSchema] = None
    total_initial_cost: Optional[TotalInitialCostSchema] = None
    monthly_expense: Optional[MonthlyExpenseSchema] = None


class HouseSchema(BaseSchema):
    id: int
    title: str
    name: str
    description: str
    price: int
    house_tags: Optional[list[HouseTagSchema]] = None


class HouseSchemaOnce(HouseSchema):
    bedrooms_count: int = Field(gt=1, le=99)
    bathrooms_count: int = Field(gt=1, le=99)
    area: int
    key_features: Optional[list[KeyFeaturesSchema]] = None
    house_photos: Optional[list[HousePhotoSchema]] = None
    city: CitySchema
    property_type: PropertyTypeSchema
    pricing_details: Optional[PricingDetailsSchema] = None


class FormAboutHouseSchemaAdd(BaseSchemaWithPhone):
    first_name: str
    last_name: str
    email: EmailStr
    house_id: int
    message: str


class FormAboutHouseSchema(FormAboutHouseSchemaAdd):
    id: int
    house: HouseSchemaOnce
