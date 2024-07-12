from pydantic import BaseModel


class BaseSchema(BaseModel):
    class Config:
        from_attributes = True # Позволяет работать не только с объектами типа dict, но и с полями объектов модели
