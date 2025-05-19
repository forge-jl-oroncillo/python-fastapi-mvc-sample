# FastAPI with Prisma MVC

This is a FastAPI application using Prisma as the database client, structured in an MVC pattern.

## Project Structure

```
app/
├── controllers/     # Handle request/response logic
├── models/         # Pydantic models/schemas
├── routes/         # API routes
├── services/       # Business logic
└── database.py     # Database configuration
```

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Initialize Prisma:
```bash
npx prisma generate
npx prisma db push
```

3. Run the application:
```bash
uvicorn main:app --reload
```

## API Documentation

Once the application is running, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Available Endpoints

### Users
- GET /users - List all users
- GET /users/{user_id} - Get a specific user
- POST /users - Create a new user
- DELETE /users/{user_id} - Delete a user

### Posts
- GET /posts - List all posts
- GET /posts/{post_id} - Get a specific post
- POST /posts/{author_id} - Create a new post
- PUT /posts/{post_id} - Update post status
