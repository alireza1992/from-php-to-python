"""Unit tests for the player-registration use case.

These tests deliberately replace external dependencies (database, Celery and
email) so that they can run without MySQL, Redis, or an SMTP server.
"""

import asyncio
import os
import sys
from types import ModuleType
from types import SimpleNamespace

import pytest
from sqlalchemy.exc import IntegrityError


# Settings are instantiated during application-module imports.  Supplying safe
# test defaults keeps this test independent of a developer's local .env file.
_SETTINGS = {
    "DB_HOST": "localhost",
    "DB_PORT": "3306",
    "DB_USER": "test",
    "DB_PASSWORD": "test",
    "DB_NAME": "skillcup_test",
    "JWT_SECRET": "test-secret",
    "MAIL_USERNAME": "test",
    "MAIL_PASSWORD": "test",
    "MAIL_FROM": "test@example.com",
    "MAIL_FROM_NAME": "SkillCup Test",
    "MAIL_PORT": "1025",
    "MAIL_SERVER": "localhost",
    "MAIL_STARTTLS": "false",
    "MAIL_SSL_TLS": "false",
    "SINGED_URL_KEY": "test-signing-key",
    "APP_URL": "https://skillcup.test",
}
for key, value in _SETTINGS.items():
    os.environ.setdefault(key, value)

# The local virtual environment contains a cryptography binary built for a
# different architecture.  Registration only needs PyJWT's two public calls,
# so a small stand-in keeps this use-case test isolated from that binary.
jwt_stub = ModuleType("jwt")
jwt_stub.encode = lambda payload, key, algorithm: f"test-token-for-{payload['sub']}"
sys.modules["jwt"] = jwt_stub

from application.usecases import register_player
from application.usecases.register_player import RegisterPlayer
from domain.identity.exceptions import UniqueConstraintException
from presentation.schemas.requests.register import RegisterValidation


class FakePlayerRepository:
    def __init__(self, player):
        self.player = player
        self.inserted_entity = None

    async def insert(self, entity):
        self.inserted_entity = entity
        return self.player


class DuplicateEmailRepository:
    async def insert(self, entity):
        raise IntegrityError(statement=None, params=None, orig=Exception("duplicate email"))


class QueuedVerificationEmail:
    def __init__(self):
        self.calls = []

    def delay(self, email, verification_url):
        self.calls.append((email, verification_url))


def test_register_player_persists_player_queues_verification_and_returns_token(monkeypatch):
    player = SimpleNamespace(
        id=42,
        email="player@example.com",
        username="skill-player",
        status=3,
    )
    repository = FakePlayerRepository(player)
    queued_email = QueuedVerificationEmail()
    monkeypatch.setattr(register_player.tasks, "send_verification_email", queued_email)

    result = asyncio.run(
        RegisterPlayer(repository).execute(
            RegisterValidation(email="player@example.com", password="secure-password")
        )
    )

    assert repository.inserted_entity.email == "player@example.com"
    assert repository.inserted_entity.password_hash == "secure-password"
    assert result.player.id == 42
    assert result.player.email == "player@example.com"
    assert result.message == "ثبت نام موفقیت آمیز بود."
    assert result.token == "test-token-for-42"
    assert len(queued_email.calls) == 1
    assert queued_email.calls[0][0] == "player@example.com"
    assert queued_email.calls[0][1].startswith("https://skillcup.test/verify-email/42/")


def test_register_player_reports_duplicate_email_without_sending_email(monkeypatch):
    queued_email = QueuedVerificationEmail()
    monkeypatch.setattr(register_player.tasks, "send_verification_email", queued_email)

    with pytest.raises(UniqueConstraintException) as error:
        asyncio.run(
            RegisterPlayer(DuplicateEmailRepository()).execute(
                RegisterValidation(email="player@example.com", password="secure-password")
            )
        )

    assert error.value.status_code == 409
    assert error.value.errors == {"email": ["این ایمیل قبلا ثبت شده است."]}
    assert queued_email.calls == []
