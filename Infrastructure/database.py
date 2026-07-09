from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

engine= create_async_engine("mysql+aiomysql://skillcup:skillcup@db:3306/skillcup")

async def get_db():
    async with AsyncSession(engine) as session:
         yield session

# Type alias
DbSession = Annotated[AsyncSession, Depends(get_db)]