from fastapi import Depends

from application.contracts.email import EmailProtocol
from application.contracts.token import TokenProtocol
from application.usecases.register_player import RegisterPlayer
from application.usecases.verify_player import PlayerEmailVerification
from domain.identity.services.email_verification import VerifyPlayer as VerifyPlayerService
from infrastructure.auth.token_service import JWTTokenService
from infrastructure.notifications.celery_email_service import CeleryEmailService
from infrastructure.repository.player_repository import PlayerRepository
from infrastructure.security.singed_url import SignedUrl


def get_email_service() -> EmailProtocol:
    return CeleryEmailService()


def get_token_service() -> JWTTokenService:
    return JWTTokenService()


def get_singed_url_service() -> SignedUrl:
    return SignedUrl()

def get_player_repository() -> PlayerRepository:
    return PlayerRepository()


def get_verify_player_service(url_service: SignedUrl = Depends(SignedUrl),player_repository: PlayerRepository = Depends(PlayerRepository) ) -> VerifyPlayerService:
    return VerifyPlayerService(url_service, player_repository)

def get_register_use_case(
        player_repository: PlayerRepository = Depends(PlayerRepository),
        celery_mail: EmailProtocol = Depends(get_email_service),
        token_service: TokenProtocol = Depends(get_token_service),
        url_maker: SignedUrl = Depends(get_singed_url_service),
) -> RegisterPlayer:
    return RegisterPlayer(player_repository, celery_mail, token_service, url_maker)


def get_player_verify_use_case(
        player_verification_service: VerifyPlayerService = Depends(get_verify_player_service),
        celery_mail: CeleryEmailService = Depends(get_email_service),
) -> PlayerEmailVerification:
    return PlayerEmailVerification(player_verification_service, celery_mail)
