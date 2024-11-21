from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Класс валидации переменных окружения"""
    
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    DATABASE_URL: str

    model_config = SettingsConfigDict(env_file=".env", case_sensitive=True, extra="allow")


settings = Settings()