from fastapi import Depends

from application.contracts.email_service import EmailService
from application.contracts.token_service import TokenService
from application.usecases.register_player import RegisterPlayer
from infrastructure.auth.token_service import JWTTokenService
from infrastructure.notifications.celery_email_service import CeleryEmailService
from infrastructure.repository.player_repository import PlayerRepository


def get_email_service() -> EmailService:
    return CeleryEmailService()

def get_token_service() -> JWTTokenService:
    return JWTTokenService()

def get_register_use_case(
        player_repository: PlayerRepository = Depends(PlayerRepository),
        celery_mail: EmailService = Depends(get_email_service),
        token_service: TokenService = Depends(get_token_service)
) -> RegisterPlayer:
    return RegisterPlayer(player_repository,celery_mail, token_service)