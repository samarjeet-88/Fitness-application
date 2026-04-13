from sqlalchemy import Column,Integer,String

from database.db_base import Base


class User(Base):
    __tablename__="users"

    id=Column(String, primary_key=True,index=True)
    full_name=Column(String,nullable=False)
    email=Column(String,nullable=False)
    password=Column(String,nullable=False)
    