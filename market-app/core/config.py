from pydantic import BaseModel
from pydantic_settings import BaseSettings


class AppRunConfig(BaseModel):
    host: str = "localhost"
    port: int = 8000


class ApiPrefix(BaseModel):
    prefix: str = "/api"


class Settings(BaseSettings):
    app_run: AppRunConfig = AppRunConfig()
    api_prefix: ApiPrefix = ApiPrefix()


settings = Settings()
