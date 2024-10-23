from fastapi import APIRouter

from core.config import settings

from .categories import router as categories_router

router = APIRouter(
    prefix=settings.api_prefix.v1.v1_prefix,
)
router.include_router(categories_router)
