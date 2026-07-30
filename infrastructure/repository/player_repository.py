from sqlalchemy import select

from domain.player.entities.player import Player as PlayerEntity
from infrastructure.database import DbSession
from infrastructure.models.player import Player as  PlayerModel


class PlayerRepository:
    def __init__(self, session : DbSession = DbSession):
        self.session = session

    async def get_by_email(self,email : str):
        query = await self.session.execute(
            select(PlayerModel).where(PlayerModel.email == email)
        )
        return query.scalar_one_or_none()

    async def insert(self, payload: PlayerEntity) -> PlayerModel:
        db_model = PlayerModel(
            email = payload.email,
            password = payload.password_hash,
            username = payload.username,
            status = payload.status.value
        )

        self.session.add(db_model)
        await self.session.flush()
        await self.session.commit()
        return db_model
