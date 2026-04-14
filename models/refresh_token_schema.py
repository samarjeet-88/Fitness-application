from sqlalchemy import Column,Integer,String,DateTime,ForeignKey
from database.db_base import Base


class User(Base):
    __tablename__="users"

    user_id=Column(String, ForeignKey("users.id"),index=True)
    token_hash=Column(String,nullable=False)
    expires_at=Column(DateTime,nullable=false)