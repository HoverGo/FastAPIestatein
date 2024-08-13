from abc import abstractmethod


class AbstractRepository():
    """Базовый репозиторий, содержащий в себе базовые абстрактные методы"""
    
    @abstractmethod
    async def create():
        pass


    @abstractmethod
    async def get_all():
        pass


    @abstractmethod
    async def get_one():
        pass
