from fastapi import FastAPI, Depends
import logging


from Infrastructure.database import DbSession
from sqlalchemy import text

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


@app.get("/")
def root(db: DbSession):

    result = db.execute(text("SELECT 2"))
    logger.info(result.all())

    return {"message": "SkillCup API is running"}
