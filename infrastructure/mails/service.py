from fastapi_mail import ConnectionConfig
from fastapi_mail import FastMail
from fastapi_mail import MessageSchema
from fastapi_mail import MessageType

from settings import settings


class MailService:

    def __init__(self):
        self.config = ConnectionConfig(
            MAIL_USERNAME=settings.mail_username,
            MAIL_PASSWORD=settings.mail_password,

            MAIL_FROM=settings.mail_from,
            MAIL_FROM_NAME=settings.mail_from_name,

            MAIL_SERVER=settings.mail_server,
            MAIL_PORT=settings.mail_port,

            MAIL_STARTTLS=settings.mail_starttls,
            MAIL_SSL_TLS=settings.mail_ssl_tls,

            USE_CREDENTIALS=False, #only for dev

            VALIDATE_CERTS=False, #only for dev
        )

    async def send_verification_email(
            self,
            email: str,
            verification_url: str,
    ) -> None:
        html = f"""
        <h2>Welcome!</h2>

        <p>
            Please verify your email.
        </p>

        <a href="{verification_url}">
            Verify Email
        </a>
        """

        message = MessageSchema(
            subject="Verify your email",
            recipients=[email],
            body=html,
            subtype=MessageType.html,
        )

        fm = FastMail(self.config)

        await fm.send_message(message)

    async def send_welcome_email(self, email: str, is_google_auth: bool = False) -> None:
        html = f"""
               <h2>Welcome to our site!</h2>

               <p>
                   It's time for you to shine!
               </p>

              
               """

        message = MessageSchema(
            subject="Welcome to SkillCup!",
            recipients=[email],
            body=html,
            subtype=MessageType.html,
        )

        fm = FastMail(self.config)

        await fm.send_message(message)

