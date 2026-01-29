from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    TRIPLOGIC_STYTCH_PROJECTID: str
    TRIPLOGIC_STYTCH_SECRET: str
    TRIPLOGIC_STYTCH_CLIENTID: str
    TRIPLOGIC_STYTCH_CLIENTSECRET: str
    PRODUCTION: str = "0"
    STAGING: str = "0"
    PYCHARM_HOSTED: str = "0"
    class Config:
        env_file = ".env"


settings = Settings()
