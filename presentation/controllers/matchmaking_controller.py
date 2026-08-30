from fastapi import Depends, APIRouter
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from application.usecases.find_opponent import FindAnOpponent
from infrastructure.auth.token_service import JWTTokenService
from presentation.schemas.requests.matchmaking import MatchmakingValidation
from presentation.dependencies.matchmaking_dependencies import get_jwt_credentials,get_matchmaking_use_case

router = APIRouter(tags=["matchmaking"])
security = HTTPBearer()


@router.post('/search')
async def matchmaking(payload: MatchmakingValidation,
                      credentials: HTTPAuthorizationCredentials = Depends(get_jwt_credentials),
                      use_case: FindAnOpponent = Depends(get_matchmaking_use_case)
                      ):
    decoded_jwt = JWTTokenService.decode(credentials)
    player_id = int(decoded_jwt.sub)
    return await  use_case.execute(player_id,payload.xp_level)
