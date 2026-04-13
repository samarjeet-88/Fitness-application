from fastapi import FastAPI
from config.env_config import settings
from database.db_connection import engine
from models.user_schema import User
from database.db_base import Base

Base.metadata.create_all(bind=engine)



app=FastAPI()


@app.get("/system-health")
def system_health():
    return {"status":"ok"}

@app.get("/env-check")
def env_check():
    return {"db_host": settings.DB_HOST, "db_name": settings.DB_NAME, "db_user": settings.DB_USER}