from argon2 import PasswordHasher as Argon2Hasher
from argon2.exceptions import  VerificationError


class PasswordHasher:
    _hasher = Argon2Hasher()
    @classmethod
    def hash(cls, password: str) -> str:
        return cls._hasher.hash(password)

    @classmethod
    def verify(cls,password: str, stored_hash: str):
        try:
            return cls._hasher.verify(stored_hash, password)
        except VerificationError:
            return False
