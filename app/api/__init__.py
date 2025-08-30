from fastapi import APIRouter
from . import user, post, profile, meta

api_router = APIRouter()
api_router.include_router(user.router, prefix="/users", tags=["Users"])
api_router.include_router(post.router, prefix="/posts", tags=["Posts"])
api_router.include_router(profile.router, prefix="/profiles", tags=["Profiles"])
api_router.include_router(meta.router, tags=["Meta"])
