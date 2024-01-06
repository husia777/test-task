

from dataclasses import dataclass
from datetime import datetime
from typing import NewType

UserId = NewType("UserId", int)


@dataclass
class UserEntity:
    id: UserId
    name: str
    email: str
    registered_at: datetime
