from pydantic import BaseModel, Field


class UserCreate(BaseModel):
    name: str = Field(max_length=50)
    email: str
