from fastapi import APIRouter
from ..service.naver_search import naver_search
router = APIRouter()


@router.get("/search")
async def search():
    return naver_search.get_news('네이버', 1000)