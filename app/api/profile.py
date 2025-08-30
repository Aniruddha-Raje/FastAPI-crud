from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.schemas.profile import Profile
from app.services.user import get_profile_by_user_id
from app.schemas.response import APIResponse

router = APIRouter()

@router.get(
    "/{user_id}",
    response_model=APIResponse,
    summary="Get profile by user ID",
    description="Retrieve the profile information for a specific user"
)
def get_profile(user_id: int, db: AsyncSession = Depends(get_db)):
    profile = get_profile_by_user_id(db, user_id)
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    return APIResponse(success=True, message="", data=profile).model_dump()
