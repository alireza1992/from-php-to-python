from infrastructure.celery.tasks import send_verification_email

class CeleryEmailService:
    @staticmethod
    def send_verification_email(email: str, verification_url: str) -> None:
         send_verification_email.delay(email, verification_url)
