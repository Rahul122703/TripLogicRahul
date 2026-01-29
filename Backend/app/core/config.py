from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    TRIPLOGIC_STYTCH_PROJECTID: str
    TRIPLOGIC_STYTCH_SECRET: str
    TRIPLOGIC_STYTCH_CLIENTID: str
    TRIPLOGIC_STYTCH_CLIENTSECRET: str

    PRODUCTION: str | None = None
    STAGING: str | None = None
    PYCHARM_HOSTED: str | None = None

    class Config:
        env_file = ".env"


settings = Settings()
