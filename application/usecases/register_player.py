import logging
from sqlalchemy.exc import IntegrityError

from application.contracts.email_service import EmailService
from application.contracts.token_service import TokenService
from domain.player.entities.player import Player as PlayerEntity
from domain.player.exceptions import UniqueConstraintException
from infrastructure.repository.player_repository import PlayerRepository
from infrastructure.security.singed_url import SignedUrl
from presentation.schemas.requests.register import RegisterValidation
from presentation.schemas.responses.register import RegisterResponse, PlayerResponse

logger = logging.getLogger(__name__)

class RegisterPlayer:
    def __init__(self, repository: PlayerRepository, celery_mail: EmailService, token_service: TokenService):
        self.repo = repository
        self.celery_mail = celery_mail
        self.jwt_token_service = token_service

    async def execute(self, payload: RegisterValidation):
        entity_object = PlayerEntity(email=payload.email, password_hash=payload.password)
        try:
            player = await self.repo.insert(entity_object)
        except IntegrityError:
            logger.warning(f"Registration attempt failed; duplicate email : {payload.email}")
            raise UniqueConstraintException(field='email')

        singed_url = SignedUrl(player.id, player.email).create()

        # Send verification email
        self.celery_mail.send_verification_email(entity_object.email, singed_url)


        token = self.jwt_token_service.issue(player.id)

       ### TODO: Handle referrals


        return RegisterResponse(token=token,
                                player= PlayerResponse.model_validate(player),
                                message="ثبت نام موفقیت آمیز بود."
                                )


