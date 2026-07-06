# This file is used to configure the application settings using Pydantic's BaseSettings. It defines a Settings class that reads the database URL from an environment variable specified in a .env file. The settings instance can be used throughout the application to access configuration values.
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    gemini_api_key: str

    class Config:
        env_file = ".env"

settings = Settings()