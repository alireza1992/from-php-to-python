from typing import Protocol

class EmailService(Protocol):
     def send_verification_email(self, email: str, url: str) -> None:
        ...
