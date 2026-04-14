from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app_config.env_config import settings

engine=create_engine(settings.DB_URL,echo=False,pool_size=5,max_overflow=10,pool_timeout=30)
# this is the postgre connection, executes SQL. "echo=True" means to print the sql queries in console.


SessionLocal=sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)
