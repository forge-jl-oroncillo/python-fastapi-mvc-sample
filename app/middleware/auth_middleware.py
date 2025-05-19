from fastapi import Request, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.responses import JSONResponse
from jose import JWTError, jwt
from datetime import datetime, timedelta
import os
from typing import Optional, Dict

# Get JWT settings from environment variables
JWT_SECRET = os.getenv("JWT_SECRET", "your-super-secret-key-change-this-in-production")
JWT_ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

security = HTTPBearer()

def create_access_token(data: Dict) -> str:
    """Create a new access token"""
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, JWT_SECRET, algorithm=JWT_ALGORITHM)

def decode_token(token: str) -> Dict:
    """Decode and verify a JWT token"""
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        if datetime.fromtimestamp(payload.get("exp")) < datetime.utcnow():
            raise H(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token has expired"
            )
        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials"
        )

async def verify_token(credentials: HTTPAuthorizationCredentials = security) -> Dict:
    if (not credentials or not credentials.credentials):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials"
        )

    """Verify the access token"""
    return decode_token(credentials.credentials)

def setup_auth(app) -> None:
    """Setup authentication middleware"""
    @app.middleware("http")
    async def auth_middleware(request: Request, call_next):
        # Skip auth for certain paths
        if request.url.path in ["/docs", "/redoc", "/openapi.json", "/", "/health", "/auth/login", "/auth/register"]:
            return await call_next(request)

        # Get authorization header
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content={"detail": "Missing or invalid authorization header"}
            )

        try:
            token = auth_header.split(" ")[1]
            payload = await verify_token(HTTPAuthorizationCredentials(scheme="Bearer", credentials=token))
            # Add user info to request state
            request.state.user = payload
            return await call_next(request)
        except HTTPException as e:
            return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content={"detail": str(e.detail) if e.detail else "Invalid authentication"}
            )
        except Exception as e:
            return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content={"detail": "Invalid authentication"}
            )

        return await call_next(request)
