"""
Using their email when registering
"""
from application.contracts.email import EmailProtocol
from domain.identity.services.email_verification import VerifyPlayer


class PlayerEmailVerification:
    def __init__(self, service: VerifyPlayer, celery_mail : EmailProtocol):
        self.service = service
        self.celery_mail = celery_mail

    async def execute(self, player_id: int, email_hashed_data: str, expires: int, signature: str) -> bool:
       player = await self.service.get_by_id(player_id)
       already_verified = self.service.already_verified(player)

       if already_verified:
           return False

       is_verifiable = self.service.url_check(email_hashed_data, player_id, player.email, expires, signature)

       if not is_verifiable:
            return False

       await self.service.verify_player(player)

       self.celery_mail.send_welcome_email(player.email)

       return True



