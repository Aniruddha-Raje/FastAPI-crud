import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")  # default if not set
