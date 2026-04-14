
from validators.auth_validator import UserRegister
from core.ApiErrorHandler import ApiErrorHandler
import bcrypt
from jose import jwt
from datetime import datetime,timedelta
from app_config.env_config import settings
from sqlalchemy import text
from database.db_connection import SessionLocal

class AuthService:


    async def hash_password(password:str)->str:
        salt=bcrypt.gensalt()
        hashed=await bcrypt.hashpw(password.encode('utf-8'),salt)
        return hashed.decode('utf-8') 

    async def verify_password(password:str,hashed_password:str)->bool:
        return await bcrypt.checkpw(password.encode('utf-8'),hashed_password.encode('utf-8'))

    async def create_access_token(data:dict):
        to_encode=data.copy()
        expire=datetime.utcnow()+timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

        to_encode.update({"exp":expire})

        access_token=jwt.encode(to_encode,settings.ACCESS_SECRET_KEY,algorithm="HS256")
        return access_token

    
    async def create_refresh_token(data:dict):
        to_encode=data.copy()
        expire=datetime.utcnow()+timedelta(minutes=settings.REFRESH_TOKEN_EXPIRE_MINUTES)

        to_encode.update({"exp":expire})

        refresh_token=jwt.encode(to_encode,settings.REFRESH_SECRET_KEY,algorithm="HS256")
        return refresh_token
    
    async def register_service(user:UserRegister):

        full_name=user.full_name
        email=user.email
        password=user.password
        confirm_password=user.confirm_password

        if(password!=confirm_password){
            raise ApiErrorHandler.bad_request()
        }

        const id=
        
        with SessionLocal.begin() as db:
            db.execute(text("INSERT INTO users u ()"))




        



