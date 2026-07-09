from typing import Annotated

from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
engine= create_engine("mysql+mysqldb://skillcup:skillcup@db:3306/skillcup")

def get_db():
    with Session(engine) as session:
         yield session

# Type alias
DbSession = Annotated[Session, Depends(get_db)]
