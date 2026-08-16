from infrastructure.celery.tasks import send_verification_email, send_welcome_email


class CeleryEmailService:
    @staticmethod
    def send_verification_email(email: str, verification_url: str) -> None:
         send_verification_email.delay(email, verification_url)

    @staticmethod
    def send_welcome_email(email:str, is_google_auth:bool = False):
        send_welcome_email.delay(email,is_google_auth)