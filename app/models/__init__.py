from .user import UserBase, UserCreate, User
from .post import PostBase, PostCreate, Post

# Resolve forward references
Post.update_forward_refs(User=User)
User.update_forward_refs(Post=Post)

__all__ = [
    'UserBase',
    'UserCreate',
    'User',
    'PostBase',
    'PostCreate',
    'Post',
]
