from pydantic import BaseModel, PostgresDsn, computed_field
from pydantic_core import MultiHostUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppRunConfig(BaseModel):
    host: str = "localhost"
    port: int = 8000


class ApiPrefix(BaseModel):
    prefix: str = "/api"


class DatabaseConfig(BaseModel):
    db_user: str
    db_password: str
    db_host: str
    db_port: int
    db_name: str
    echo_sql: bool = False
    echo_pool: bool = False
    pool_size: int = 5
    max_overflow: int = 10
    
    @computed_field
    @property
    def asyncpg_url(self) -> PostgresDsn:
        return MultiHostUrl.build(
            scheme="postgresql+asyncpg",
            username=self.db_user,
            password=self.db_password,
            host=self.db_host,
            port=self.db_port,
            path=self.db_name,
        )

    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True, case_sensitive=False)


class Settings(BaseSettings):
    app_run: AppRunConfig = AppRunConfig()
    api_prefix: ApiPrefix = ApiPrefix()
    db: DatabaseConfig = DatabaseConfig()


settings = Settings()
