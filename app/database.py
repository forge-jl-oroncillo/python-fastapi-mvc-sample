from prisma import Prisma

# Initialize Prisma client
prisma = Prisma()

async def init_db():
    await prisma.connect()

async def close_db():
    if prisma.is_connected():
        await prisma.disconnect()
