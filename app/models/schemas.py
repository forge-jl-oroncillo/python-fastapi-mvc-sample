from pydantic import BaseModel
from typing import Optional, List

class UserBase(BaseModel):
    email: str
    name: Optional[str] = None

class PostBase(BaseModel):
    title: str
    content: Optional[str] = None
    published: bool = False

class PostCreate(PostBase):
    pass

class UserCreate(UserBase):
    pass

class Post(PostBase):
    id: int
    author_id: Optional[int] = None

    class Config:
        from_attributes = True

class User(UserBase):
    id: int
    posts: List[Post] = []

    class Config:
        from_attributes = True
