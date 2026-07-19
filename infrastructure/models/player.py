from datetime import datetime
from typing import List, Optional

from sqlalchemy import String, func, FetchedValue, Index
from sqlalchemy.dialects.mysql import DATETIME
from sqlalchemy.orm import Mapped, mapped_column, relationship

from infrastructure.models.base import Base


class Player(Base):
    __tablename__ = 'players'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    username: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    status: Mapped[int] = mapped_column(nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=True)
    email_verified_at: Mapped[str] = mapped_column(DATETIME, nullable=True)
    google_id: Mapped[str] = mapped_column(String(255), nullable=True)
    referral_code: Mapped[str] = mapped_column(String(255), nullable=True)
    phone_number: Mapped[str] = mapped_column(String(255), nullable=True)
    avatar: Mapped[str] = mapped_column(String(255), nullable=True)
    twitch_username: Mapped[str] = mapped_column(String(255), nullable=True)
    youtube_username: Mapped[str] = mapped_column(String(255), nullable=True)
    telegram_username: Mapped[str] = mapped_column(String(255), nullable=True)
    instagram_username: Mapped[str] = mapped_column(String(255), nullable=True)
    favourite_player: Mapped[str] = mapped_column(String(255), nullable=True)
    favourite_team: Mapped[str] = mapped_column(String(255), nullable=True)
    sheba: Mapped[str] = mapped_column(String(255), nullable=True)
    ea_id: Mapped[str] = mapped_column(String(255), nullable=True)
    deactivation_reason: Mapped[int] = mapped_column(nullable=True)
    xp: Mapped[int] = mapped_column(nullable=True)
    is_fake: Mapped[bool] = mapped_column(default=False, nullable=True)
    is_admin: Mapped[bool] = mapped_column(default=False, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DATETIME, nullable=True, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DATETIME, nullable=True, server_onupdate=FetchedValue())

    # (Composite) Indexes
    __table_args__ = (
        Index(
            "ix_player_username",
            "username",
        ),
        Index(
            "ix_search_id_status",
            "id",
            "status",
        ),
    )

    # Relationships
    chats: Mapped[List["Chat"]] = relationship(back_populates="player", cascade="all, delete-orphan")
    rewards: Mapped[List["Reward"]] = relationship(back_populates="player", cascade="all, delete-orphan")
    payments: Mapped[List["Payment"]] = relationship(back_populates="player", cascade="all, delete-orphan")
    matches: Mapped[List["Match"]] = relationship(back_populates="player", cascade="all, delete-orphan")
    credit: Mapped[Optional["Credit"]] = relationship(back_populates="player", cascade="all, delete-orphan", uselist=False)
    searches: Mapped[List["Search"]] = relationship(back_populates="player", cascade="all, delete-orphan")
