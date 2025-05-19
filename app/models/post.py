from pydantic import BaseModel
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .user import User

class PostBase(BaseModel):
    title: str
    content: Optional[str] = None
    published: bool = False

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    author_id: Optional[int] = None
    author: Optional['User'] = None

    class Config:
        from_attributes = True
        populate_by_name = True
