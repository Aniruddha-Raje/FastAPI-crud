from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.logger import logger
from app.api.user import router
from app.core.auth import auth_middleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.middleware("http")(auth_middleware)

app.include_router(router, prefix="/users", tags=["Users"])

@app.get("/")
def root():
    logger.info("Root endpoint called")
    return {"message": "Welcome to FastAPI App"}
