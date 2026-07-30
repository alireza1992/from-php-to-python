from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class PlayerResponse(BaseModel):
    model_config = {"from_attributes": True}

    id: int
    email: str
    username: str
    status: int
    name: Optional[str] = None
    email_verified_at: Optional[datetime] = None
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
    deactivation_reason: Optional[int] = None
    xp: Optional[int] = None
    is_fake: Optional[bool] = False
    is_admin: Optional[bool] = False
    referrer_id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    # TODO : add stats and claimable_rewards and favourite_badges and current_credit


class RegisterResponse(BaseModel):
    token: str
    player: PlayerResponse
    message: Optional[str] = None
