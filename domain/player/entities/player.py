from datetime import datetime
from typing import Optional
from dataclasses import dataclass, field
from domain.player.enums.deactivation import DeactivationReason
from domain.player.enums.status import PlayerStatus
from domain.player.enums.xp import XP
from domain.shared.string_generator import StringGenerator


@dataclass(eq=False, kw_only=True, slots=True)
class Player:
    id: Optional[int] = None
    email: str
    password_hash: str
    username: str= field(default_factory=StringGenerator.generate_random_string)
    status: PlayerStatus = PlayerStatus.NOT_VERIFIED

    is_fake: Optional[bool] = False
    is_admin: Optional[bool] = False
    name: Optional[str] = None
    email_verified_at: Optional[datetime] = None
    google_id: Optional[str] = None
    referral_code: Optional[str] = None
    phone_number: Optional[str] = None
    avatar: Optional[str] = None
    twitch_username: Optional[str] = None
    youtube_username: Optional[str] = None
    telegram_username: Optional[str] = None
    instagram_username: Optional[str] = None
    favourite_player: Optional[str] = None
    favourite_team: Optional[str] = None
    sheba: Optional[str] = None
    ea_id: Optional[str] = None
    deactivation_reason: Optional[DeactivationReason] = None
    xp: Optional[XP] = None

    def __eq__(self, other: object) -> bool:
        return (
            isinstance(other,self.__class__) and
            self.id == other.id
        )

    def __hash__(self) -> int:
        return hash((self.__class__, self.id))

    def verify_player(self, when: Optional[datetime] = None) -> None:
        """
        Only when player clicks on the verification link in the email, this method will be called.
        :return: None
        """
        when = datetime.now() if when is None else when
        self.email_verified_at = when if self.email_verified_at is None else self.email_verified_at
        self.status = PlayerStatus.ACTIVE.value

    @property
    def is_active(self) -> bool:
        return self.status == PlayerStatus.ACTIVE.value

    @property
    def needs_email_verification(self):
        return self.email_verified_at is None

    @property
    def is_faker(self) -> bool:
        return self.is_fake
