import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import ClassVar


class Settings(BaseSettings):
	ROOT: str = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

	model_config: ClassVar[SettingsConfigDict] = SettingsConfigDict(env_file=os.path.join(ROOT, ".env"))

	DOMAIN: str
	ENVIRONMENT: str

	FIRST_SUPERUSER: str
	FIRST_SUPERUSER_PASSWORD: str

	POSTGRES_SERVER: str
	POSTGRES_PORT: int
	POSTGRES_DB: str
	POSTGRES_USER: str
	POSTGRES_PASSWORD: str

	DOCKER_IMAGE_FRONTEND: str
	DOCKER_IMAGE_BACKEND: str


config = Settings()
