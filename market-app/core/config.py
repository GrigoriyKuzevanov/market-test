from pydantic import BaseModel
from pydantic_settings import BaseSettings


class RunAppConfig(BaseModel):
    host: str = "192.168.7.248"
    port: int = 8000
    reload: bool = True


class ApiPrefixConfig(BaseModel):
    prefix: str = "/api"


class Settings(BaseSettings):
    run_app: RunAppConfig = RunAppConfig()
    api_prefix: ApiPrefixConfig = ApiPrefixConfig()


settings = Settings()
