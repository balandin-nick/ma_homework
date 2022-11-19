from pydantic import Field, SecretStr

from app.settings.base import AdvancedBaseSettings


__all__ = [
    "ServiceDatabaseSettings",
    "service_database_settings",
]


class ServiceDatabaseSettings(AdvancedBaseSettings):
    host: str
    username: str
    password: SecretStr
    db_name: str = Field(..., env="service_db_name")
    port: int = Field(default="5432")

    class Config:
        env_prefix = "service_db_"

    @property
    def postgresql_url(self) -> str:
        return f"postgresql://{self.username}:{self.password.get_secret_value()}" \
               f"@{self.host}:{self.port}/{self.db_name}"


service_database_settings = ServiceDatabaseSettings()
