import logging
from src.presentation.web_api.providers.abstract.user import user_service_provider
from src.adapters.db.connection import get_session
from src.adapters.db.repositories.user_repositories import UserRepository
from src.interactors.user.user_service import UserService
from src.presentation.web_api.endpoints.user import user_router
from fastapi import FastAPI, Depends

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()],
)
app = FastAPI()

app.include_router(user_router)


def get_user_repository(session=Depends(get_session)):
    return UserRepository(session)


def get_user_service(user_repository=Depends(get_user_repository)):
    return UserService(user_repository)


app.dependency_overrides[user_service_provider] = get_user_service
