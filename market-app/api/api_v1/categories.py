from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from api.api_v1.crud.category import get_all_categories,  create_category
from core.config import settings
from core.models import db_connector
from core.schemas.category import CategoryOut, CategoryCreate

router = APIRouter(
    prefix=settings.api_prefix.v1.categories,
    tags=["Categories"],
)


@router.get("", response_model=list[CategoryOut])
async def get_categories(session: AsyncSession = Depends(db_connector.get_session)):
    categories = await get_all_categories(session=session)
    return categories

@router.post("", response_model=CategoryOut, status_code=status.HTTP_201_CREATED)
async def post_category(category_create: CategoryCreate, session: AsyncSession = Depends(db_connector.get_session)):
    category = await create_category(session=session, category_create=category_create)
    return category
