from abc import abstractmethod


class BaseRepository():

    @abstractmethod
    async def create():
        pass


    @abstractmethod
    async def get_all():
        pass


