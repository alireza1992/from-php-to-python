from fastapi import Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.ext.asyncio import AsyncSession
from application.contracts.player import PlayerProtocol
from application.usecases.find_opponent import FindAnOpponent
from infrastructure.database import get_db
from infrastructure.repository.player_repository import PlayerRepository

security = HTTPBearer()


def get_jwt_credentials(credentials: HTTPAuthorizationCredentials = Depends(security)) -> str:
    return credentials.credentials


def get_player_repository(
        session: AsyncSession = Depends(get_db),
) -> PlayerProtocol:
    return PlayerRepository(session)


def get_matchmaking_use_case(player_repository: PlayerProtocol = Depends(get_player_repository)) -> FindAnOpponent:
    return FindAnOpponent(player_repository)
