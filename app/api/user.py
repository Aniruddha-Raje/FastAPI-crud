from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.schemas.user import UserCreate, User
from app.services import user as user_service
from app.schemas.response import APIResponse

router = APIRouter()

@router.post(
    "/",
    response_model=APIResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new user",
    description="Creates a user with optional profile data"
)
def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    return APIResponse(success=True, message="", data=user_service.create_user(db, user)).model_dump()

@router.get(
    "/",
    response_model=APIResponse,
    summary="List all users",
    description="Fetch a list of all users with their profiles and posts"
)
def list_users(db: AsyncSession = Depends(get_db)):
    return APIResponse(success=True, message="", data=user_service.get_users(db)).model_dump()

@router.get(
    "/{user_id}",
    response_model=APIResponse,
    summary="Get a user by ID",
    description="Retrieve a single user by their ID"
)
def get_user(user_id: int, db: AsyncSession = Depends(get_db)):
    user = user_service.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return APIResponse(success=True, message="", data=user).model_dump()

@router.delete(
    "/{user_id}",
    response_model=APIResponse,
    status_code=status.HTTP_200_OK,
    summary="Delete a user",
    description="Deletes a user and associated profile/posts"
)
def delete_user(user_id: int, db: AsyncSession = Depends(get_db)):
    return APIResponse(success=True, message="", data=user_service.delete_user(db, user_id)).model_dump()
