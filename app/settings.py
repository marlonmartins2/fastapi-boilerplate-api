from pydantic import BaseSettings


class Settings(BaseSettings):
    """
    load environments from .env file
    :param BaseSettings: Pydantic BaseSettings
    """

    class Config:
        env_file = './.env'

    APP_NAME: str
    APP_ENV: str
    APP_DESCRIPTION: str
    CORS_ORIGINS: list
    ENVIRONMENT: str
    DEBUG: bool

    # Database
    MONGO_URL: str
    MONGO_SSL: str
    PATH_CERT: str
    DATABASE_ENVIRONMENT: str

    # Sentry
    SENTRY_URL: str
    SENTRY_ENVIRONMENT: str


settings = Settings()