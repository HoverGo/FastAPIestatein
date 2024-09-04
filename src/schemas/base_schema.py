from pydantic import BaseModel, field_validator
import re


class BaseSchema(BaseModel):
    class Config:
        from_attributes = True  # Позволяет работать не только с объектами типа dict, но и с полями объектов модели


class BaseSchemaWithPhone(BaseSchema):

    phone: str

    @field_validator("phone")
    def phone_validator(cls, v):
        phone_pattern = r"^(\+)[1-9][0-9\-\(\)\.]{9,15}$"

        if not re.match(phone_pattern, v):
            raise ValueError("Phone do not match")

        return v
