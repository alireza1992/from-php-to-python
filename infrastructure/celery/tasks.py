import asyncio
from infrastructure.celery.app import celery
from infrastructure.mails.service import MailService


@celery.task
def send_verification_email(email: str, verification_url: str):
    service = MailService()
    asyncio.run(
        service.send_verification_email(email, verification_url)
    )

@celery.task
def send_welcome_email(email: str,is_google_auth:bool= False):
    service = MailService()
    asyncio.run(
        service.send_welcome_email(email, is_google_auth)
    )
