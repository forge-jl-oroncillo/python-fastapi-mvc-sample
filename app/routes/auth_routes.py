from fastapi import APIRouter, HTTPException, status
from app.controllers.user_controller import UserController
from app.models.users import UserCreate, User, UserLogin
from app.middleware import create_access_token

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=User, status_code=status.HTTP_201_CREATED)
async def register(user: UserCreate):
    # Check if user already exists
    existing_user = await UserController.get_user_by_email(user.email)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    # Create new user
    return await UserController.create_user(user)


@router.post("/login")
async def login(user_data: UserLogin):
    print(user_data)
    # Verify user credentials
    user = await UserController.get_user_by_email(user_data.email)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )
    
    # In a real application, verify password here
    # if not verify_password(user_data.password, user.hashed_password):
    #     raise HTTPException(
    #         status_code=status.HTTP_401_UNAUTHORIZED,
    #         detail="Invalid credentials"
    #     )
    
    # Generate access token
    access_token = create_access_token({
        "sub": str(user.id),
        "email": user.email
    })
    
    return {"access_token": access_token, "token_type": "bearer"}
