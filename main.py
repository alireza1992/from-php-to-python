from fastapi import FastAPI, Form
import logging
from pydantic import BaseModel
from Infrastructure.database import DbSession
from sqlalchemy import text
import jwt
from config import Settings, settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


@app.get("/")
async def root(db: DbSession):

    result = await db.execute(text("SELECT 2"))
    logger.info(result.all())

    return {"message": "SkillCup API is running"}

class UserIn(BaseModel):
    username: str
    password: str

@app.post("/register")
async def register(user:UserIn):
    to_encode = {"sub": user.username}
    token = jwt.encode(to_encode, settings.jwt_secret, algorithm="HS256")
    return {"token":token }
