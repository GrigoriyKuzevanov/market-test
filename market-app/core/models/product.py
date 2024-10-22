from decimal import Decimal

from sqlalchemy import DECIMAL, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base_model import Base


class Product(Base):
    __tablename__ = "products"

    name: Mapped[str] = mapped_column(nullable=False, unique=True)
    price: Mapped[Decimal] = mapped_column(DECIMAL(10, 2), nullable=False)
    category_id: Mapped[int] = mapped_column(
        ForeignKey("categories.id", ondelete="CASCADE"), nullable=False
    )
    category: Mapped["Category"] = relationship("Category", back_populates="products")
