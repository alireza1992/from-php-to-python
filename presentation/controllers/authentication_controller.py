from typing import Annotated

from fastapi import APIRouter
from fastapi.params import Depends, Path, Query

from application.usecases.register_player import RegisterPlayer
from application.usecases.verify_player import  PlayerEmailVerification
from presentation.schemas.requests.register import RegisterValidation
from presentation.dependencies.player_dependencies import get_register_use_case, get_player_verify_use_case

router = APIRouter(tags=["Authentication"])


@router.post('/register')
async def register(payload: RegisterValidation, use_case: RegisterPlayer = Depends(get_register_use_case)):
    result = await use_case.execute(payload)
    return result

@router.get('/verify-email/{player_id}/{hashed_email}')
async def verify_email(
        player_id: Annotated[int, Path(title="Id of the player to be verified", gt=0)],
        hashed_email: Annotated[str, Path(title="email to be decoded")],
        expires: Annotated[int, Query(title="Timestamp")],
        signature: Annotated[str, Query(title="Decodes the secret")],
        use_case: PlayerEmailVerification = Depends(get_player_verify_use_case)
):
    return await use_case.execute(player_id, hashed_email, expires, signature)

# TODO: login needs to be implemented