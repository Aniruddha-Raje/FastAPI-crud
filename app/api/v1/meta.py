from fastapi import APIRouter, status
from app.core.config import settings

router = APIRouter()

@router.get(
    "/healthcheck",
    status_code=status.HTTP_200_OK,
    summary="Health Check",
    description="Simple health check endpoint to verify if the service is up"
)
def healthcheck():
    return {"status": "ok"}

@router.get(
    "/version",
    status_code=status.HTTP_200_OK,
    summary="Get App Version",
    description="Returns the current version of the application"
)
def version():
    return {"version": settings.APP_VERSION}
