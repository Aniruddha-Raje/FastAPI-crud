from pydantic import BaseModel
from typing import List, Optional
from app.schemas.post import Post  # Referenced only
from app.schemas.profile import Profile  # Referenced only

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    profile: Optional[Profile] = None  # Input can accept profile info

class User(UserBase):
    id: int
    profile: Optional[Profile] = None
    posts: List[Post] = []

    class Config:
        orm_mode = True
