from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.api_v1.crud.category import get_all_categories
from core.config import settings
from core.models import db_connector
from core.schemas.category import CategoryOut

router = APIRouter(
    prefix=settings.api_prefix.v1.categories,
    tags=["Categories"],
)


@router.get("", response_model=list[CategoryOut])
async def get_categories(session: AsyncSession = Depends(db_connector.get_session)):
    categories = await get_all_categories(session=session)
    return categories
