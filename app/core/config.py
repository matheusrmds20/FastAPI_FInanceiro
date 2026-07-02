from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME: str = "Finance app"
    DEBUG: bool = True

    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    model_config=SettingsConfigDict(env_file=".env")

    DATABASE_URL: str = "postgresql://postgres.lwupfanslrqaxwsvxonm:25304318Ma.@aws-1-sa-east-1.pooler.supabase.com:6543/postgres"

settings = Settings()
