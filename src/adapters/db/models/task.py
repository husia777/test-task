from sqlalchemy.orm import mapped_column, Mapped

from src.infrastructure.db.connection import Base


class Task(Base):
    __tablename__ = 'task'
    id: Mapped[int] = mapped_column(
        primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
