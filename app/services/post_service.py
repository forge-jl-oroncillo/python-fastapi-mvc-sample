from app.database import prisma
from app.models.post import PostCreate, Post
from typing import List, Optional

class PostService:
    @staticmethod
    async def create_post(post: PostCreate, author_id: int) -> Post:
        return await prisma.post.create(
            data={
                'title': post.title,
                'content': post.content,
                'published': post.published,
                'author': {
                    'connect': {'id': author_id}
                }
            }
        )
    
    @staticmethod
    async def get_post(post_id: int) -> Optional[Post]:
        return await prisma.post.find_unique(
            where={
                'id': post_id
            },
            include={
                'author': True
            }
        )
    
    @staticmethod
    async def get_posts() -> List[Post]:
        return await prisma.post.find_many(
            include={
                'author': True
            }
        )
    
    @staticmethod
    async def update_post(post_id: int, published: bool) -> Post:
        return await prisma.post.update(
            where={
                'id': post_id
            },
            data={
                'published': published
            }
        )
