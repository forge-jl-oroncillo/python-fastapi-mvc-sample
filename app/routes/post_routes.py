from fastapi import APIRouter
from app.controllers.post_controller import PostController
from app.models.schemas import PostCreate, Post
from typing import List

router = APIRouter(prefix="/posts", tags=["posts"])

@router.post("/{author_id}", response_model=Post)
async def create_post(author_id: int, post: PostCreate):
    return await PostController.create_post(post, author_id)

@router.get("/{post_id}", response_model=Post)
async def get_post(post_id: int):
    return await PostController.get_post(post_id)

@router.get("/", response_model=List[Post])
async def get_posts():
    return await PostController.get_posts()

@router.put("/{post_id}", response_model=Post)
async def update_post(post_id: int, published: bool):
    return await PostController.update_post(post_id, published)
