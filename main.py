from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.database import init_db, close_db
from app.routes import user_routes, post_routes
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize DB connection on startup
    try:
        await init_db()
        yield
    finally:
        # Close DB connection on shutdown
        await close_db()

app = FastAPI(
    title="FastAPI with Prisma MVC",
    description="A RESTful API built with FastAPI and Prisma ORM using MVC pattern",
    version="1.0.0",
    lifespan=lifespan,
    openapi_url="/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc"
)

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"detail": str(exc)}
    )

# Include routers
app.include_router(user_routes.router)
app.include_router(post_routes.router)

@app.get("/", tags=["root"])
async def root():
    """Welcome endpoint that returns a greeting message"""
    return {"message": "Welcome to FastAPI with Prisma MVC!"}

@app.get("/health", tags=["health"])
async def health_check():
    """Health check endpoint for monitoring"""
    try:
        # Check database connection
        await prisma.user.count()
        return {
            "status": "healthy",
            "database": "connected",
            "timestamp": datetime.datetime.utcnow().isoformat()
        }
    except Exception as e:
        return {
            "status": "unhealthy",
            "database": str(e),
            "timestamp": datetime.datetime.utcnow().isoformat()
        }