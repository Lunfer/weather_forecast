# config.py

import os
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

class Config:
    API_URL = "https://api.meteomatics.com"
    API_USERNAME = os.getenv("API_USERNAME")
    API_PASSWORD = os.getenv("API_PASSWORD")
    LOCATIONS = [
        "35.6895,139.6917",  # Coordinates for Tokyo, Japan
        "40.7128,-74.0060",  # Coordinates for New York, USA
        "48.8566,2.3522",  # Coordinates for Paris, France
    ]
    DB_URL = os.getenv("DATABASE_URL", "sqlite:///weather.db")
