from abc import ABC, abstractmethod
from sqlalchemy import select, delete, update
from sqlalchemy.orm import Session
from src.adapters.db.models.user import User
from src.domain.task.entities.user import UserEntity, UserId
from sqlalchemy.ext.asyncio import AsyncSession


class UserRepositoryInterface(ABC):

    @abstractmethod
    async def create_user(self, user: UserEntity):
        pass

    @abstractmethod
    async def get_all_users(self) -> list[UserEntity]:
        pass

    async def get_user_by_id(self, id: int) -> UserEntity:
        pass

    async def remove_user_by_id(self, id: int):
        pass


class UserRepository(UserRepositoryInterface):

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_user(self, user: UserEntity):
        async with self.session.begin():
            user = User(**user.dict())
            self.session.add(user)

    async def get_all_users(self) -> list[UserEntity]:
        async with self.session.begin():
            users = await self.session.execute(select(User))
            return users.scalars().all()

    async def get_user_by_id(self, id: UserId) -> UserEntity:
        async with self.session.begin():
            user = await self.session.execute(select(User).where(User.id == id))
            return user.scalars().first()

    async def remove_user_by_id(self, id: UserId):
        async with self.session.begin():
            await self.session.execute(delete(User).where(User.id == id))
