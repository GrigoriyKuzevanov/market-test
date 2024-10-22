from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base_model import Base


class Category(Base):
    __tablename__ = "categories"

    name: Mapped[str] = mapped_column(nullable=False, unique=True)
    products: Mapped[list["Product"]] = relationship(
        "Product", back_populates="category"
    )
