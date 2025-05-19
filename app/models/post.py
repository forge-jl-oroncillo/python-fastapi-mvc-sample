from pydantic import BaseModel
from typing import Optional
class PostBase(BaseModel):
    title: str
    content: Optional[str] = None
    published: bool = False

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    author_id: Optional[int] = None

    class Config:
        from_attributes = True

