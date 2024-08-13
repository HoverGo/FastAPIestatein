from src.repositories.base_repository import BaseRepository
from src.schemas.question_form_schema import QuestionFormSchema, QuestionFormSchemaAdd


class QuestionFormRepository(BaseRepository):
    
    
    async def create(self, question_form_data: QuestionFormSchemaAdd) -> QuestionFormSchemaAdd:
        question_form = await super().create(question_form_data)
        return question_form
    

    async def get_all(self) -> list[QuestionFormSchema]:
        question_forms = await super().get_all()
        return question_forms