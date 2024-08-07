from src.services.base_service import BaseService
from src.repositories.house_form_repository import HouseFormRepository
from src.models.house_form_model import HouseForm
from src.schemas.house_form_schema import HouseFormSchemaAdd


class HouseFormService(BaseService):

    repository = HouseFormRepository
    model = HouseForm

    async def create(self, schema: HouseFormSchemaAdd):
        instance = await super().create(schema, self.repository, self.model)
        return instance

    async def get_all(self):
        queryset = await super().get_all(self.repository, self.model)
        return queryset


class HouseFormDataService(BaseService):
    
    async def get_all(self):
        pass