import datetime
import hmac
import hashlib
from datetime import timedelta
from settings import settings


class SignedUrl:
    @staticmethod
    def create(player_id: int, email: str) -> str:
        expires: datetime.datetime = datetime.datetime.now(datetime.timezone.utc) + timedelta(minutes=15)
        hash_id_and_email_and_expiry = hmac.new(
            key=settings.singed_url_key.encode(),
            msg=f"{player_id}.{email}.{int(expires.timestamp())}".encode(),
            digestmod=hashlib.sha256
        ).hexdigest()
        email_hash = hashlib.sha1(email.encode()).hexdigest()
        url = f"{settings.app_url}/verify-email/{player_id}/{email_hash}?expires={int(expires.timestamp())}&signature={hash_id_and_email_and_expiry}"

        return url

    @staticmethod
    def email_verification_hash_check(hashed_email_in_url: str,
                                      player_id: int,
                                      email: str,
                                      expires: int,
                                      signature: str) -> bool:


        player_email_hash = hashlib.sha1(email.encode()).hexdigest()
        if not hmac.compare_digest(player_email_hash, hashed_email_in_url):
            return False

        rehash_url_data = hmac.new(
            key=settings.singed_url_key.encode(),
            msg=f"{player_id}.{email}.{expires}".encode(),
            digestmod=hashlib.sha256
        ).hexdigest()

        return hmac.compare_digest(rehash_url_data, signature)
