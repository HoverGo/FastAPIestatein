from src.services.base_service import BaseService
from src.repositories.question_form_repository import QuestionFormRepository
from src.models.question_form_model import QuestionForm
from src.schemas.question_form_schema import QuestionFormSchema, QuestionFormSchemaAdd


class QuestionFormService(BaseService):
    
    
    repository = QuestionFormRepository
    model = QuestionForm


    async def create(self, question_form_schema: QuestionFormSchemaAdd) -> QuestionFormSchemaAdd:
        question_form = await super().create(question_form_schema, self.repository, self.model)
        return question_form
    

    async def get_all(self) -> list[QuestionFormSchema]:
        question_forms = await super().get_all(self.repository, self.model)
        return question_forms