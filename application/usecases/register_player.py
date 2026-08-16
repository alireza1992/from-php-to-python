import logging
from sqlalchemy.exc import IntegrityError

from application.contracts.email import EmailProtocol
from application.contracts.token import TokenProtocol
from domain.identity.entities.player import Player as PlayerEntity
from domain.identity.exceptions import UniqueConstraintException
from infrastructure.repository.player_repository import PlayerRepository
from infrastructure.security.password_hasher import PasswordHasher
from infrastructure.security.singed_url import SignedUrl
from presentation.schemas.requests.register import RegisterValidation
from presentation.schemas.responses.register import RegisterResponse, PlayerResponse

logger = logging.getLogger(__name__)

class RegisterPlayer:
    def __init__(self, repository: PlayerRepository, celery_mail: EmailProtocol, token_service: TokenProtocol, url_maker: SignedUrl):
        self.repo = repository
        self.celery_mail = celery_mail
        self.jwt_token_service = token_service
        self.url_maker = url_maker

    async def execute(self, payload: RegisterValidation):
        hashed_password = PasswordHasher.hash(payload.password)  ## infra's concern - need contract here
        entity_object = PlayerEntity(email=payload.email, password_hash=hashed_password)
        try:
            player = await self.repo.insert(entity_object)
        except IntegrityError:
            logger.warning(f"Registration attempt failed; duplicate email : {payload.email}")
            raise UniqueConstraintException(field='email')

        # Send verification email
        singed_url = self.url_maker.create(player.id, player.email)
        self.celery_mail.send_verification_email(entity_object.email, singed_url)


        token = self.jwt_token_service.issue(player.id)

       ### TODO: Handle referrals


        return RegisterResponse(token=token,
                                player= PlayerResponse.model_validate(player),
                                message="ثبت نام موفقیت آمیز بود."
                                )
        ## application is below presentation and does not know about presentation! wrong return , should be application respose .

