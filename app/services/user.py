from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException, status
from app.models import User, Post, Profile
from app.schemas import UserCreate, PostCreate
from app.core.logger import logger
from typing import List

def create_user(db: AsyncSession, user: UserCreate):
    db_user = User(username=user.username)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    logger.info(f"User created: {db_user.username}")
    return db_user

def get_users(db: AsyncSession):
    result = db.execute(select(User))
    return result.scalars().all()

# ✅ Get user by ID
def get_user_by_id(user_id: int, db: AsyncSession) -> User:
    result = db.execute(select(User).where(User.id == user_id))
    user = result.scalars().first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID {user_id} not found"
        )
    return user


# ✅ Delete user by ID
def delete_user(user_id: int, db: AsyncSession) -> dict:
    user = get_user_by_id(user_id, db)
    db.delete(user)
    db.commit()
    return {"message": f"User with ID {user_id} deleted successfully"}

def get_profile_by_user_id(user_id: int, db: AsyncSession) -> Profile:
    result = db.execute(select(Profile).where(Profile.user_id == user_id))
    profile = result.scalars().first()
    if not profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Profile for User ID {user_id} not found"
        )
    return profile

def get_posts(user_id: int, db: AsyncSession) -> List[Post]:
    result = db.execute(select(Post).where(Post.user_id == user_id))
    posts = result.scalars().all()
    if not posts:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No posts found for User ID {user_id}"
        )
    return posts

def create_post(post_in: PostCreate, db: AsyncSession) -> Post:
    # Ensure the user exists before assigning the post
    user_result = db.execute(select(User).where(User.id == post_in.user_id))
    user = user_result.scalars().first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID {post_in.user_id} not found"
        )

    post = Post(**post_in.dict())
    db.add(post)
    db.commit()
    db.refresh(post)
    return post