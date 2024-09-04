from src.schemas.base_schema import BaseSchema, BaseSchemaWithPhone
from pydantic import EmailStr


class QuestionFormSchemaAdd(BaseSchemaWithPhone):
    """Форма для задаваний вопросов"""

    first_name: str
    last_name: str
    email: EmailStr
    inquiry_type: str
    way_to_find: str
    message: str


class QuestionFormSchema(QuestionFormSchemaAdd):
    id: int
