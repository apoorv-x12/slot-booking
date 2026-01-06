import os
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import text
from dotenv import load_dotenv

load_dotenv()

engine = create_async_engine(
    os.getenv("DATABASE_URL"),
    pool_size=5,
    max_overflow=0,
    echo=True
)

async def execute(query: str, params: dict = {}):
    async with engine.begin() as conn:
        result = await conn.execute(text(query), params)
        return result
