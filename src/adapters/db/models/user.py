from datetime import datetime
import email
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy.sql import func
from sqlalchemy import String, DateTime

from src.adapters.db.connection import Base


class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(
        primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    registered_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now())
