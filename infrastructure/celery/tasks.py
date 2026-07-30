import asyncio
from infrastructure.celery.app import celery
from infrastructure.mails.service import MailService

@celery.task
def send_verification_email(email: str, verification_url: str):
    service = MailService()
    asyncio.run(
        service.send_verification_email(email, verification_url)
    )