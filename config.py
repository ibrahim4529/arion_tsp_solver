from pydantic import BaseSettings

class Settings(BaseSettings):
    DB_NAME: str = "arion"
    DB_TYPE: str = "mysql"
    DB_HOST: str = "localhost"
    DB_PORT: int = 3306
    DB_USER: str = "root"
    DB_PASSWORD: str = "root"
    MAPS_API_KEY: str =""
    
    class Config:
        env_file = ".env"


def get_config():
    return Settings()