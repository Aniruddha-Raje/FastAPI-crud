from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.schemas.post import PostCreate, Post
from app.services import post as post_service

router = APIRouter()

@router.post(
    "/",
    response_model=Post,
    status_code=status.HTTP_201_CREATED,
    summary="Create a post",
    description="Create a post and associate it with a user via user_id query parameter"
)
async def create_post(post: PostCreate, user_id: int = Query(...), db: AsyncSession = Depends(get_db)):
    return await post_service.create_post(db, post, user_id)

@router.get(
    "/",
    response_model=list[Post],
    summary="List all posts",
    description="Fetch a list of all posts from all users"
)
async def list_posts(db: AsyncSession = Depends(get_db)):
    return await post_service.get_posts(db)
