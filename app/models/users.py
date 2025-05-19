from pydantic import BaseModel
from typing import Optional, List
from app.models.post import Post

class UserBase(BaseModel):
    email: str
    name: Optional[str] = None

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    posts: Optional[List[Post]] = []

    class Config:
        from_attributes = True
