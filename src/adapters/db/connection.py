from sqlalchemy.pool import NullPool
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from src.adapters.db.config import settings


engine = create_async_engine(
    settings.sqlalchemy_database_url, echo=True, future=True,
    poolclass=NullPool,
)
async_session = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession
)


class Base(DeclarativeBase):
    pass


async def get_session() -> async_session:
    async with async_session() as session:
        yield session
