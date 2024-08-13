from src.models.base_model import BaseModel
from sqlalchemy.orm import Mapped


class QuestionForm(BaseModel):
    __tablename__ = "question_form"

    first_name: Mapped[str]
    last_name: Mapped[str]
    email: Mapped[str]
    phone: Mapped[str]
    inquiry_type: Mapped[str]
    way_to_find: Mapped[str]
    message: Mapped[str]

