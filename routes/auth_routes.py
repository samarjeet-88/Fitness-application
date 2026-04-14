from fastapi import APIRouter
from fastapi import Request
from validators.user_validator import UserRegister


router=APIRouter()

@router.post("/register")
async def register(user:UserRegister,request:Request):
    

