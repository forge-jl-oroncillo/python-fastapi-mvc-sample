from pydantic import BaseModel
from typing import Optional, List, ForwardRef

# Use ForwardRef for Post to avoid circular imports
Post = ForwardRef('Post')

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
        populate_by_name = True