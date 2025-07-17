from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.core.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)

    # Relationships (still here but not their definitions)
    profile = relationship("Profile", uselist=False, back_populates="user")
    posts = relationship("Post", back_populates="user")
