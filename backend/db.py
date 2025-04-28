import ssl
import os
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Create SSL context
ssl_context = ssl.create_default_context()

# Create async engine
engine = create_async_engine(
    DATABASE_URL,
    echo=True,
    connect_args={"ssl": ssl_context}  # <-- this tells asyncpg to use SSL
)

# Session factory
async_session = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession
)

# Dependency to use in routes
async def get_db():
    async with async_session() as session:
        yield session
