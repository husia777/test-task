
from src.domain.task.entities.user import UserEntity


class UserService:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    async def get_all_users(self):
        return await self.user_repository.get_all_users()

    async def get_user_by_id(self, id: int):
        return await self.user_repository.get_user_by_id(id)

    async def remove_user_by_id(self, id: int):
        return await self.user_repository.remove_user_by_id(id)

    async def create_user(self, user: UserEntity):
        return await self.user_repository.create_user(user)
