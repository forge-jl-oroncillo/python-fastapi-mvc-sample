from fastapi import HTTPException
from app.models.post import PostCreate, Post
from app.services.post_service import PostService
from typing import List

class PostController:
    @staticmethod
    async def create_post(post: PostCreate, author_id: int) -> Post:
        try:
            return await PostService.create_post(post, author_id)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
    
    @staticmethod
    async def get_post(post_id: int) -> Post:
        post = await PostService.get_post(post_id)
        if not post:
            raise HTTPException(status_code=404, detail="Post not found")
        return post
    
    @staticmethod
    async def get_posts() -> List[Post]:
        return await PostService.get_posts()
    
    @staticmethod
    async def update_post(post_id: int, published: bool) -> Post:
        try:
            return await PostService.update_post(post_id, published)
        except Exception as e:
            raise HTTPException(status_code=404, detail="Post not found")
