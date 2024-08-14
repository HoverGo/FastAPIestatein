from src.services.base_service import BaseService
from src.schemas.review_schema import ReviewSchema, ReviewAddSchema, CompanyReviewSchema, CompanyReviewAddSchema
from src.repositories.review_repository import ReviewRepository, CompanyReviewRepository
from src.models.review_model import Review, CompanyReview


class ReviewService(BaseService):

    repository = ReviewRepository
    model = Review


    async def create(self, review_schema: ReviewAddSchema) -> ReviewAddSchema:
        review = await super().create(review_schema, self.repository, self.model)
        return review
    

    async def get_all(self) -> list[ReviewSchema]:
        reviews = await super().get_all(self.repository, self.model)
        return reviews
    

class CompanyReviewService(BaseService):
    
    repository = CompanyReviewRepository
    model = CompanyReview

    async def create(self, company_review_schema: CompanyReviewAddSchema) -> CompanyReviewAddSchema:
        company_review = await super().create(company_review_schema, self.repository, self.model)
        return company_review
    

    async def get_all(self) -> list[CompanyReviewSchema]:
        company_reviews = await super().get_all(self.repository, self.model)
        return company_reviews