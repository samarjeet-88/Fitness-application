from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_HOST:str
    DB_PORT:int
    DB_USER:str 
    DB_PASSWORD:str
    DB_NAME:str
    DB_URL:str
    ACCESS_SECRET_KEY:str
    ACCESS_TOKEN_EXPIRE_MINUTES:int
    REFRESH_SECRET_KEY:str
    REFRESH_TOKEN_EXPIRE_MINUTES:int

    class Config:
        env_file=".env"


settings=Settings()


