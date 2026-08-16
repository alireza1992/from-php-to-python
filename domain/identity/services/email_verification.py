import datetime
from typing import Optional

from domain.exceptions.RecordNotFoundException import RecordNotFoundException
from infrastructure.models.player import Player as PlayerModel
from infrastructure.repository.player_repository import PlayerRepository
from infrastructure.security.singed_url import SignedUrl


class VerifyPlayer:
    def __init__(self, url_service: SignedUrl, repository: PlayerRepository):
        self.url_service = url_service
        self.repository = repository

    async def get_by_id(self, player_id: int) -> Optional[PlayerModel]:
        player = await self.repository.get_by_id(player_id)
        if player is None:
            raise RecordNotFoundException("Player")
        return player

    @staticmethod
    def already_verified(player: PlayerModel) -> bool:
        if player.email_verified_at is not None:
            return True
        return False

    def url_check(self, email_hashed_data: str, player_id: int, user_email: str, expires: int, signature: str) -> bool:
        now = datetime.datetime.now(datetime.timezone.utc)
        if expires <= int(now.timestamp()):
            return False
        return self.url_service.email_verification_hash_check(email_hashed_data, player_id, user_email, expires, signature)

    async def verify_player(self, player: PlayerModel) -> None:
       return  await self.repository.verify_player(player.id)
