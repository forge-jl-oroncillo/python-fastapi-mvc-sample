# Use Python 3.11 slim image
FROM python:3.11-slim

# Install Node.js for Prisma
RUN apt-get update && apt-get install -y \
    curl \
    && curl -sL https://deb.nodesource.com/setup_18.x | bash - \
    && apt-get install -y nodejs \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy Python requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy package.json and install Node dependencies
COPY package.json .
RUN npm install

# Copy Prisma schema
COPY prisma ./prisma/

# Set a build-time DATABASE_URL for Prisma client generation
ARG DATABASE_URL=postgresql://postgres:postgres@db:5432/postgres?schema=public
ENV DATABASE_URL=${DATABASE_URL}

# Generate Prisma client and fetch Python binaries
RUN npx prisma generate \
    && python -m prisma generate \
    && python -m prisma py fetch

# Copy the rest of the application
COPY . .

# Expose portweb
EXPOSE 8000

# Create entrypoint script
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Start the application
CMD ["/entrypoint.sh"]
