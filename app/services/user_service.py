from app.database import prisma
from app.models.users import UserCreate, User
from typing import List

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
        user = await prisma.user.find_unique(
            where={
                'id': user_id
            }
        )
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        return await prisma.user.delete(
            where={
                'id': user_id
            }
        )

    @staticmethod
    async def get_user_by_email(email: str) -> User:
        return await prisma.user.find_unique(
            where={
                'email': email
            }
        )
