# app/core/config.py

import os
from dotenv import load_dotenv

# Load from .env file
load_dotenv()

# Read environment variables
DATABASE_URL = os.getenv("DATABASE_URL")
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")  # default if not set
