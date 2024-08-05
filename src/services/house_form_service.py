from src.services.base_service import BaseService
from src.repositories.house_form_repository import HouseFormRepository
from src.models.house_form_model import HouseForm


class HouseFormService(BaseService):

    repository = HouseFormRepository
    model = HouseForm

    async def get_all(self):
        queryset = await super().get_all(self.repository, self.model)
        return queryset
