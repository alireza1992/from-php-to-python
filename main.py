from fastapi import Request
from fastapi import FastAPI
import logging.config
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from domain.exceptions.base import DomainException
from log_config import LOGGING_CONFIG
from presentation.middlewares.register import register_middlewares
from presentation.controllers.authentication_controller import router as authentication_router
from presentation.controllers.matchmaking_controller import router as matchmaking_router

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)
app = FastAPI()

# Register middlewares
register_middlewares(app)

app.include_router(authentication_router)
app.include_router(matchmaking_router)



@app.exception_handler(DomainException)
async def domain_exception_handler(request: Request, exc: DomainException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "message": exc.message,
            "errors": exc.errors
        }
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = {}
    for error in exc.errors():
        field = error["loc"][-1]  # last part of location = field name
        errors.setdefault(field, []).append(error["msg"])

    return JSONResponse(
        status_code=422,
        content={
            "message": "اطلاعات وارد شده معتبر نمی‌باشد",
            "errors": errors
        }
    )