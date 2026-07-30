import datetime
import hmac
import hashlib
from datetime import timedelta
from settings import settings


class SignedUrl:
    def __init__(self, player_id: int, email: str):
        self.player_id = player_id
        self.email = email

    def create(self) -> str:
        hash_id_and_email = hmac.new(
            key=settings.singed_url_key.encode(),
            msg=f"{self.player_id}.{self.email}".encode(),
            digestmod=hashlib.sha256
        ).hexdigest()
        email_hash = hashlib.sha1(self.email.encode()).hexdigest()
        expires = datetime.datetime.now(datetime.timezone.utc) + timedelta(minutes=15)
        url = f"{settings.app_url}/verify-email/{self.player_id}/{email_hash}?expires={int(expires.timestamp())}&signature={hash_id_and_email}"

        return url

    def hash_check(self, expected_hash: str, player_id: int, email: str):
        pass