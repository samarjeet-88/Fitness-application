from fastapi import FastAPI
from app_config.env_config import settings
from database.db_connection import engine
from models.user_schema import User
from database.db_base import Base
from fastapi import Request
from core.ApiErrorHandler import ApiErrorHandler
from middlewares.global_error_handler import api_exception_handler,validation_exception_handler
from fastapi.exceptions import RequestValidationError

Base.metadata.create_all(bind=engine)


app=FastAPI()

# global error handler
@app.add_exception_handler(ApiErrorHandler,api_exception_handler)
@app.add_exception_handler(RequestValidationError,validation_exception_handler)


@app.get("/system-health")
def system_health():
    return {"status":"ok"}

@app.get("/env-check")
def env_check():
    return {"db_host": settings.DB_HOST, "db_name": settings.DB_NAME, "db_user": settings.DB_USER}