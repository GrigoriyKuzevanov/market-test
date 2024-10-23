from pydantic import BaseModel, PostgresDsn, computed_field
from pydantic_core import MultiHostUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppRunConfig(BaseModel):
    host: str = "localhost"
    port: int = 8000


class ApiV1Prefix(BaseModel):
    v1_prefix: str = "/v1"
    categories: str = "/categories"


class ApiPrefix(BaseModel):
    prefix: str = "/api"
    v1: ApiV1Prefix = ApiV1Prefix()


class DatabaseConfig(BaseModel):
    pg_user: str
    pg_password: str
    pg_host: str
    pg_port: int
    pg_name: str
    echo_sql: bool = False
    echo_pool: bool = False
    pool_size: int = 5
    max_overflow: int = 10

    @computed_field
    @property
    def asyncpg_url(self) -> PostgresDsn:
        return MultiHostUrl.build(
            scheme="postgresql+asyncpg",
            username=self.pg_user,
            password=self.pg_password,
            host=self.pg_host,
            port=self.pg_port,
            path=self.pg_name,
        )


class Settings(BaseSettings):
    app_run: AppRunConfig = AppRunConfig()
    api_prefix: ApiPrefix = ApiPrefix()
    db: DatabaseConfig

    model_config = SettingsConfigDict(
        # env_file=("market-app/.env.template", "market-app/.env"),
        env_file=(".env.template", ".env"),
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="APP__",
    )


settings = Settings()
