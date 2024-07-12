from abc import abstractmethod


class BaseRepository():
    """Базовый репозиторий, содержащий в себе абстрактные базовые методы"""
    
    @abstractmethod
    async def create():
        pass


    @abstractmethod
    async def get_all():
        pass


