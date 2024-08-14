from src.repositories.base_repository import BaseRepository
from src.schemas.review_schema import ReviewSchema, ReviewAddSchema, CompanyReviewSchema, CompanyReviewAddSchema


class ReviewRepository(BaseRepository):
    
    
    async def create(self, review_data: ReviewAddSchema) -> ReviewAddSchema:
        review = await super().create(review_data)
        return review
    

    async def get_all(self) -> list[ReviewSchema]:
        reviews = await super().get_all()
        return reviews
    

class CompanyReviewRepository(BaseRepository):
    
    
    async def create(self, company_review_data: CompanyReviewAddSchema) -> CompanyReviewAddSchema:
        company_review = await super().create(company_review_data)
        return company_review
    

    async def get_all(self) -> list[CompanyReviewSchema]:
        company_reviews = await super().get_all()
        return company_reviews