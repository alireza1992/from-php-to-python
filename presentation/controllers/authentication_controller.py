from fastapi import APIRouter
from fastapi.params import Depends

from application.usecases.register_player import RegisterPlayer
from presentation.schemas.requests.register import RegisterValidation
from presentation.dependencies.player_dependencies import get_register_use_case


router = APIRouter(tags=["Authentication"])


@router.post('/register')
async def register(payload: RegisterValidation, use_case: RegisterPlayer = Depends(get_register_use_case)):
    result = await use_case.execute(payload)
    return result

