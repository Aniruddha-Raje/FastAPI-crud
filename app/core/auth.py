from fastapi import Request
from fastapi.responses import JSONResponse
from app.core.logger import logger

# Example token; replace with JWT validation or DB check
SECRET_TOKEN = "mysecrettoken"

async def auth_middleware(request: Request, call_next):
    logger.info("auth_middleware")
    logger.info("path: %s, method: %s", request.url.path, request.method)

    public_paths = ["/docs", "/openapi.json"]
    if request.url.path in public_paths:
        return await call_next(request)

    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        return JSONResponse(status_code=401, content={"detail": "Authorization header missing or invalid"})

    # Extract token
    token = auth_header.split("Bearer ")[1]

    # Validate token (replace with JWT verification logic)
    if token != SECRET_TOKEN:
        return JSONResponse(status_code=401, content={"detail": "Invalid token"})

    # Token is valid → proceed
    return await call_next(request)
