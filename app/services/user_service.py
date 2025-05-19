from app.database import prisma
from app.models.schemas import UserCreate, User
from typing import List, Optional

class UserService:
    @staticmethod
    async def create_user(user: UserCreate) -> User:
        return await prisma.user.create(
            data={
                'email': user.email,
                'name': user.name
            }
        )
    
    @staticmethod
    async def get_user(user_id: int):
        return await prisma.user.find_unique(
            where={
                'id': user_id
            },
            include={
                'posts': True
            }
        )
    
    @staticmethod
    async def get_users() -> List[User]:
        return await prisma.user.find_many(
            include={
                'posts': True
            }
        )
    
    @staticmethod
    async def delete_user(user_id: int) -> User:
        return await prisma.user.delete(
            where={
                'id': user_id
            }
        )
