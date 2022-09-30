from typing import List

from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'postgresql+asyncpg://postgres:admin@localhost:5432/engenharia_rede'
    DBBaseModel = declarative_base()
    """
    import secrets

    token: str = secrets.token_urlsafe(32)
    """
    JWT_SCRET: str = '0wJX8-mFFhFsfupHUdWuePFzWDJO1WdW8rx-6Yporzg'
    ALGORITHM: str = 'HS256'

    # token valido 1 semana
    ACESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

    class Config:
        case_sensitive = True


settings: Settings = Settings()
