from fastapi import APIRouter


router = APIRouter(
   prefix="/api"
   )

@router.get("/")
async def home():
   return {"data": "Hello World"}