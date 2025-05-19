from fastapi import HTTPException
from app.models.user import UserCreate, User
from app.services.user_service import UserService
from typing import List

class UserController:
    @staticmethod
    async def create_user(user: UserCreate) -> User:
        try:
            return await UserService.create_user(user)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
    
    @staticmethod
    async def get_user(user_id: int) -> User:
        user = await UserService.get_user(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    
    @staticmethod
    async def get_users() -> List[User]:
        return await UserService.get_users()
    
    @staticmethod
    async def delete_user(user_id: int):
        try:
            return await UserService.delete_user(user_id)
        except Exception as e:
            raise HTTPException(status_code=404, detail="User not found")
