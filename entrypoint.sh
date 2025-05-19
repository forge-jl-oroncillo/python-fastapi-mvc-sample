#!/bin/bash

# Wait for database to be ready
echo "Waiting for database to be ready..."
python -m prisma db push

# Start the application
exec uvicorn main:app --host 0.0.0.0 --port 8000
