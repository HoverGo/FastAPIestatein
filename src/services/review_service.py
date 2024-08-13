from src.services.base_service import BaseService
from src.schemas.review_schema import ReviewSchema, ReviewAddSchema
from src.repositories.review_repository import ReviewRepository
from src.models.review_model import Review


class ReviewService(BaseService):

    repository = ReviewRepository
    model = Review


    async def create(self, review_schema: ReviewAddSchema) -> ReviewAddSchema:
        review = await super().create(review_schema, self.repository, self.model)
        return review
    

    async def get_all(self) -> list[ReviewSchema]:
        reviews = await super().get_all(self.repository, self.model)
        return reviews