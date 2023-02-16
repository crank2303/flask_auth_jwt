from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    pg_user: str = Field('app', env='POSTGRES_USER')
    pg_password: str = Field('123qwe', env='POSTGRES_PASSWORD')
    pg_host: str = Field('postgres', env='PG_HOST')
    pg_port: int = 5432
    db_name: str = Field('auth_database', env='POSTGRES_DB')

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = Settings()