from pydantic import BaseModel
from typing import Optional

class PostBase(BaseModel):
    title: str
    content: str

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int

    class Config:
        orm_mode = True

class PostCreate(BaseModel):
    title: str
    content: Optional[str] = None
    user_id: int