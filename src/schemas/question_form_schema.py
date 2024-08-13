from src.schemas.base_schema import BaseSchema
from pydantic import EmailStr


class QuestionFormSchemaAdd(BaseSchema):
    """ Форма для задаваний вопросов """
    first_name: str
    last_name: str
    email: EmailStr
    phone: str
    inquiry_type: str
    way_to_find: str
    message: str


class QuestionFormSchema(QuestionFormSchemaAdd):
    id: int