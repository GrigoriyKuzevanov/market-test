from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Category
from core.schemas.category import CategoryCreate


async def get_all_categories(session: AsyncSession) -> list[Category]:
    stmt = select(Category).order_by(Category.id)
    db_result = await session.scalars(stmt)
    return db_result.all()


async def create_category(session: AsyncSession, category_create: CategoryCreate) -> Category:
    category = Category(**category_create.model_dump())
    session.add(category)
    await session.commit()
    await session.refresh(category)
    return category
