from datetime import datetime
from typing import Optional
from sqlalchemy import ForeignKey, func, FetchedValue, Index
from sqlalchemy.dialects.mysql import DATETIME
from sqlalchemy.orm import Mapped, mapped_column, relationship
from domain.search.enums.status import SearchStatus
from infrastructure.models.base import Base


class Search(Base):
    __tablename__ = 'searches'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    player_id: Mapped[int] = mapped_column(ForeignKey("players.id"), nullable=False)
    xp_level: Mapped[int] = mapped_column(nullable=False)
    status: Mapped[int] = mapped_column(nullable=False, default=SearchStatus.REQUESTED.value)
    created_at: Mapped[datetime] = mapped_column(DATETIME, nullable=True, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DATETIME, nullable=True, server_onupdate=FetchedValue())

    __table_args__ = (
        Index(
            "ix_search_player_id_status",
            "player_id",
            "status",
        ),
        Index(
            "ix_search_player_id",
            "player_id",
        ),
    )

    player: Mapped[Optional["Player"]] = relationship(back_populates="searches")
