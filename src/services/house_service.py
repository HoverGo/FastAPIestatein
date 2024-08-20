from src.services.base_service import BaseService
from src.schemas.house_schema import IdFilter, CategorySchemaAdd, CategorySchema, CitySchema, CitySchemaAdd, PropertyTypeSchema, PropertyTypeSchemaAdd, HouseSchema, HouseSchemaOnce
from src.repositories.house_repository import CategoryRepository, CityRepository, PropertyTypeRepository, HouseRepository
from src.models.house_model import Category, City, PropertyType, House

class CategoryService(BaseService):

    repository = CategoryRepository
    model = Category

    async def create(self, category_schema: CategorySchemaAdd) -> CategorySchemaAdd:
        category = await super().create(category_schema, self.repository, self.model)
        return category
    

    async def get_one(self, schema: IdFilter) -> CategorySchema:
        pk = schema.model_dump()["id"]
        category = await super().get_one(self.repository, self.model, id=pk)
        return category
    

    async def get_all(self) -> list[CategorySchema]:
        categories = await super().get_all(self.repository, self.model)
        return categories
    

class CityService(BaseService):

    repository = CityRepository
    model = City

    async def create(self, city_schema: CitySchemaAdd) -> CitySchemaAdd:
        city = await super().create(city_schema, self.repository, self.model)
        return city
    

    async def get_all(self) -> list[CitySchema]:
        cities = await super().get_all(self.repository, self.model)
        return cities
    

class PropertyTypeService(BaseService):

    repository = PropertyTypeRepository
    model = PropertyType

    async def create(self, property_type_schema: PropertyTypeSchemaAdd) -> PropertyTypeSchemaAdd:
        property_type = await super().create(property_type_schema, self.repository, self.model)
        return property_type
    
    
    async def get_all(self) -> list[PropertyTypeSchema]:
        property_types = await super().get_all(self.repository, self.model)
        return property_types
                    

class HouseService(BaseService):

    repository = HouseRepository
    model = House

    async def get_all(self) -> list[HouseSchema]:
        houses = await super().get_all(self.repository, self.model)
        return houses
    

    async def get_one(self, schema: IdFilter) -> HouseSchemaOnce:
        pk = schema.model_dump()["id"]
        house = await super().get_one(self.repository, self.model, id=pk)
        return house