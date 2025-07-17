from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.schemas.user import UserCreate, User
from app.services import user as user_service

router = APIRouter()

@router.post(
    "/",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new user",
    description="Creates a user with optional profile data"
)
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    return await user_service.create_user(db, user)

@router.get(
    "/",
    response_model=list[User],
    summary="List all users",
    description="Fetch a list of all users with their profiles and posts"
)
async def list_users(db: AsyncSession = Depends(get_db)):
    return await user_service.get_users(db)

@router.get(
    "/{user_id}",
    response_model=User,
    summary="Get a user by ID",
    description="Retrieve a single user by their ID"
)
async def get_user(user_id: int, db: AsyncSession = Depends(get_db)):
    user = await user_service.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete(
    "/{user_id}",
    response_model=dict,
    status_code=status.HTTP_200_OK,
    summary="Delete a user",
    description="Deletes a user and associated profile/posts"
)
async def delete_user(user_id: int, db: AsyncSession = Depends(get_db)):
    return await user_service.delete_user(db, user_id)
