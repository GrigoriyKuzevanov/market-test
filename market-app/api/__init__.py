from fastapi import APIRouter
from .api_v1 import router as v1_router
from core.config import settings

router = APIRouter(prefix=settings.api_prefix.prefix)
router.include_router(v1_router)
