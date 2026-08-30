from datetime import timedelta, timezone, datetime
import jwt

from presentation.schemas.requests.jwt import JWTPayload
from settings import settings
import secrets


class JWTTokenService:
    @staticmethod
    def issue(player_id: int) -> str:
        payload_structure = {
            "sub": str(player_id),
            "exp": datetime.now(timezone.utc) + timedelta(hours=24),
            "iat": datetime.now(timezone.utc),
            "nbf": datetime.now(timezone.utc),
            "jti": secrets.token_urlsafe(16)
        }
        return jwt.encode(payload_structure, settings.jwt_secret, algorithm="HS256")

    @staticmethod
    def decode(token: str)-> JWTPayload:
        if token.startswith("Bearer "):
            token = token[7:]
        decoded= jwt.decode(token, settings.jwt_secret, algorithms=["HS256"])
        validated= JWTPayload.model_validate(decoded, strict=True, extra='forbid')
        return validated
