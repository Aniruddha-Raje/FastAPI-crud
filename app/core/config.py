from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    PROJECT_NAME: str = "FastAPI App"
    ALLOWED_ORIGINS: list[str] = ["*"]
    APP_VERSION: str = "1.0.0"

    class Config:
        env_file = ".env"

settings = Settings()
