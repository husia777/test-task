from fastapi import APIRouter, Depends
from src.presentation.web_api.dependencies.depends_stub import Stub
from src.presentation.web_api.providers.abstract.user import user_service_provider
from src.presentation.web_api.schemas.user import UserCreate
from src.interactors.user.user_service import UserService
from src.adapters.db.connection import get_session
user_router = APIRouter(
    tags=['users'],

)


@user_router.get('/users')
async def get_all_users(user_service: UserService = Depends(Stub(user_service_provider))):
    return await user_service.get_all_users()


@user_router.get('/users/{id}')
async def get_user_by_id(id: int, user_service: UserService = Depends(Stub(user_service_provider))):
    return await user_service.get_user_by_id(id)


@user_router.delete('/users/{id}')
async def remove_user_by_id(id: int, user_service: UserService = Depends(Stub(user_service_provider))):
    return await user_service.remove_user_by_id(id)


@user_router.post('/users')
async def create_user(user: UserCreate, user_service: UserService = Depends(Stub(user_service_provider))):
    return await user_service.create_user(user)
