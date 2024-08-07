from src.repositories.base_repository import BaseRepository
from src.models.house_model import Category
from src.schemas.house_schema import CategorySchema, CategorySchemaAdd, CitySchemaAdd, PropertyTypeSchemaAdd

class CategoryRepository(BaseRepository):


    async def create(self, category_data: CategorySchemaAdd) -> CategorySchemaAdd:
        category = await super().create(category_data)
        return category
    
    
    async def get_one(self, **filters) -> CategorySchema:
        category = await super().get_one(**filters)
        return category


    async def get_all(self) -> list[CategorySchema]:
        category_models = await super().get_all()
        categories = [
            CategorySchema.model_validate(category_model)
            for category_model in category_models
        ]
        return categories


class CityRepository(BaseRepository):


    async def create(self, city_data: CitySchemaAdd) -> CitySchemaAdd:
        city = await super().create(city_data)
        return city
    

class PropertyTypeRepository(BaseRepository):
    
    
    async def create(self, property_type_data: PropertyTypeSchemaAdd) -> CitySchemaAdd:
        property_type = await super().create(property_type_data)
        return property_type
