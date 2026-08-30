from datetime import datetime, timezone

from sqlalchemy import select, update

from domain.identity.entities.player import Player as PlayerEntity
from domain.identity.enums.status import PlayerStatus
from infrastructure.database import DbSession
from infrastructure.models.player import Player as PlayerModel


class PlayerRepository:
    def __init__(self, session: DbSession = DbSession):
        self.session = session

    async def get_by_email(self, email: str):
        query = await self.session.execute(
            select(PlayerModel).where(PlayerModel.email == email)
        )
        return query.scalar_one_or_none()

    async def get_by_id(self, player_id: int)->PlayerModel|None:
        query = await self.session.execute(
            select(PlayerModel).where(PlayerModel.id == player_id)
        )
        return query.scalar_one_or_none()

    async def insert(self, payload: PlayerEntity) -> PlayerModel:
        db_model = PlayerModel(
            email=payload.email,
            password=payload.password_hash,
            username=payload.username,
            status=payload.status.value
        )

        self.session.add(db_model)
        try:
            await self.session.flush()
            await self.session.commit()
        except:
            await self.session.rollback()
            raise
        return db_model

    async def verify_player(self, player_id: int):
        statement = (
            update(PlayerModel)
            .where(PlayerModel.id == player_id)
            .values(email_verified_at=datetime.now(timezone.utc), status=PlayerStatus.ACTIVE.value)
        )
        try:
            await self.session.execute(statement)
            await self.session.commit()
        except:
            await self.session.rollback()
            raise
        return

