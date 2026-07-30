from fastapi import FastAPI

from .cors import cors_middleware


def register_middlewares(app: FastAPI):
    cors_middleware(app)
    # app.add_middleware(RateLimitMiddleware, max_requests=60, window_seconds=60)
