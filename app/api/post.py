from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.schemas.post import PostCreate, Post
from app.services.user import create_post, get_posts
from app.schemas.response import APIResponse

router = APIRouter()

@router.post(
    "/",
    response_model=APIResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a post",
    description="Create a post and associate it with a user via user_id query parameter"
)
def create_post(post: PostCreate, user_id: int = Query(...), db: AsyncSession = Depends(get_db)):
    return APIResponse(success=True, message="", data=create_post(db, post, user_id)).model_dump()

@router.get(
    "/",
    response_model=APIResponse,
    summary="List all posts",
    description="Fetch a list of all posts from all users"
)
def list_posts(db: AsyncSession = Depends(get_db)):
    return APIResponse(success=True, message="", data=get_posts(db)).model_dump()

