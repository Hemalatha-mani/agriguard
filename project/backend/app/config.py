"""
Application configuration.

All secrets and environment-specific values are read from environment
variables (see .env.example). Nothing here is hardcoded.
"""
from functools import lru_cache
from typing import List

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # --- App ---
    APP_NAME: str = "Crop Disease Detection API"
    ENVIRONMENT: str = "development"  # development | production

    # --- Database ---
    DATABASE_URL: str  # e.g. postgresql://user:password@host:5432/dbname

    # --- Auth ---
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 24 hours

    # --- CORS ---
    # Comma-separated list of allowed origins, e.g.
    # "https://your-app.vercel.app,http://localhost:5173"
    ALLOWED_ORIGINS: str = "http://localhost:5173"

    # --- AI Model ---
    MODEL_PATH: str = "ml_models/crop_disease_model_final.keras"
    MODEL_INPUT_SIZE: int = 224

    # --- Uploads ---
    MAX_UPLOAD_SIZE_MB: int = 10

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    @property
    def cors_origins(self) -> List[str]:
        return [origin.strip() for origin in self.ALLOWED_ORIGINS.split(",") if origin.strip()]


@lru_cache
def get_settings() -> Settings:
    return Settings()
