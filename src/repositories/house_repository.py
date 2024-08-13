from src.repositories.base_repository import BaseRepository
from src.schemas.house_schema import CategorySchema, CategorySchemaAdd, CitySchema, CitySchemaAdd, PropertyTypeSchema, PropertyTypeSchemaAdd

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
    

    async def get_all(self) -> list[CitySchema]:
        city_models = await super().get_all(order="country_id")
        cities = [CitySchema.model_validate(city)
                  for city in city_models]
        return cities
    

class PropertyTypeRepository(BaseRepository):
    
    
    async def create(self, property_type_data: PropertyTypeSchemaAdd) -> CitySchemaAdd:
        property_type = await super().create(property_type_data)
        return property_type


    async def get_all(self) -> list[PropertyTypeSchema]:
        property_type_models = await super().get_all()
        property_types = [PropertyTypeSchema.model_validate(property_type)
                          for property_type in property_type_models]
        return property_types