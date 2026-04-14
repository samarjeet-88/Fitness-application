from sqlalchemy import Column,Integer,String,DateTime,func
from database.db_base import Base


class User(Base):
    __tablename__="users"

    id=Column(String, primary_key=True,index=True)
    full_name=Column(String,nullable=False)
    email=Column(String,nullable=False)
    password=Column(String,nullable=False)
    created_at=Column(DateTime,server_default=func.now(),nullable=False)
    updated_at=Column(DateTime,server_default=func.now(),onupdate=func.now(),nullable=False)