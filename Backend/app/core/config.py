from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    STYTCH_PROJECT_ID: str
    STYTCH_SECRET: str
    STYTCH_CLIENT_ID: str | None = None
    STYTCH_CLIENTSECRET: str | None = None
    ENVIRONMENT: str = "test"  # "test" or "live"
    FRONTEND_CALLBACK_URL: str = "http://localhost:5173/auth/callback"
    JWT_SECRET: str
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 24 hours by default

    class Config:
        env_file = ".env"

settings = Settings()
