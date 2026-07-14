from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from settings import settings

engine = create_async_engine(
    f"mysql+aiomysql://{settings.db_user}:{settings.db_password}@{settings.db_host}:{settings.db_port}/{settings.db_name}")


async def get_db():
    async with AsyncSession(engine) as session:
        yield session


# Type alias
DbSession = Annotated[AsyncSession, Depends(get_db)]
