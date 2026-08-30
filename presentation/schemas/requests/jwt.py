from pydantic import BaseModel


class JWTPayload(BaseModel):
    sub: str
    exp: int
    iat: int
    nbf: int
    jti: str