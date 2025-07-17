from pydantic import BaseModel

class Profile(BaseModel):
    bio: str

    class Config:
        orm_mode = True
