import os
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import text

load_dotenv()

DATABASE_URL=os.getenv("DATABASE_URL")

engine = create_async_engine(
    DATABASE_URL,
    pool_size=5,
    max_overflow=0,
    echo=True,
)

async def execute(query: str,params: dict={}):
    async with engine.begin() as conn:
        result = await conn.execute(text(query),params)
        print("ROWCOUNT:", result.rowcount)

        return result 