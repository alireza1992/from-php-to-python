from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from settings import settings

engine = create_async_engine(
    settings.db_url,
    pool_size=5,
    max_overflow=10,
    echo=True,
)

session_maker = async_sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)
async def get_db():
    async with session_maker.begin() as session: # for auto-commit
        yield session


# Type alias
DbSession = Annotated[AsyncSession, Depends(get_db)]
