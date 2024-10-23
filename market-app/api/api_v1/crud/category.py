from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Category


async def get_all_categories(session: AsyncSession) -> list[Category]:
    stmt = select(Category).order_by(Category.id)
    db_result = await session.scalars(stmt)
    return db_result.all()
