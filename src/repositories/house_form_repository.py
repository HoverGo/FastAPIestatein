from src.repositories.base_repository import BaseRepository
from src.schemas.base_schema import BaseSchema
from src.schemas.house_form_schema import HouseFormSchema

class HouseFormRepository(BaseRepository):


    async def get_all(self) -> list[HouseFormSchema]:
        house_form_models = await super().get_all()
        return house_form_models