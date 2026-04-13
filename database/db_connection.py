from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.env_config import settings

engine=create_engine(settings.DB_URL,echo=True)

SessionLocal=sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)