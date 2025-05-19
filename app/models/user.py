from pydantic import BaseModel
from typing import Optional, List

class UserBase(BaseModel):
    email: str
    name: Optional[str] = None

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    posts: List['Post'] = []

    class Config:
        from_attributes = True
        populate_by_name = True

from .post import Post  # Import at the end to avoid circular import