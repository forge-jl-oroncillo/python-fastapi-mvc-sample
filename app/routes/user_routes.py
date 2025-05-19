from fastapi import APIRouter
from app.controllers.user_controller import UserController
from app.models.schemas import UserCreate, User
from typing import List

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=User)
async def create_user(user: UserCreate):
    return await UserController.create_user(user)

@router.get("/{user_id}", response_model=User)
async def get_user(user_id: int):
    return await UserController.get_user(user_id)

@router.get("/", response_model=List[User])
async def get_users():
    return await UserController.get_users()

@router.delete("/{user_id}", response_model=User)
async def delete_user(user_id: int):
    return await UserController.delete_user(user_id)
