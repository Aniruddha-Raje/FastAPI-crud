from fastapi import Request
from app.core.logger import logger

def auth_middleware(request: Request, call_next):
    logger.info("auth_middleware")
    logger.info("path: %s, method: %s", request.url.path, request.method)

    # Add auth logic here
    return call_next(request)
