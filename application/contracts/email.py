from typing import Protocol


class EmailProtocol(Protocol):
    def send_verification_email(self, email: str, url: str) -> None:
        ...

    def send_welcome_email(self, email: str, is_google_auth: bool = False)->None:
        ...
