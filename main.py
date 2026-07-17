from fastapi import FastAPI
import logging.config

from infrastructure.exceptions.DatabaseConnectionFailedException import DatabaseConnectionFailedException
from log_config import LOGGING_CONFIG
from infrastructure.database import DbSession
from sqlalchemy import text

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)
app = FastAPI()


@app.get("/health")
async def health_check(db: DbSession):
    try:
        await db.execute(text("SELECT 1"))
        return {"status": "db is ok"}
    except DatabaseConnectionFailedException as e:
        logger.error(f"Health check failed: {e}")
        return {"status": "error"}, 500
