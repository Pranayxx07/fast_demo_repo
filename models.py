from db import BASE
from sqlalchemy import Column,Integer,String,DateTime,ForeignKey
from datetime import datetime
# from sqlalchemy.orm import For

class User(BASE):
    __tablename__= 'user'
    user_id = Column(Integer,primary_key=True,autoincrement=True)
    user_name = Column(String(500),nullable=False)
    created_at = Column(DateTime,default=datetime.now())
    updated_at = Column(DateTime,default=datetime.now())

class UserDetails(BASE):
    __tablename__ = "user_details"
    user_id = Column(Integer,ForeignKey(name='user.user_id',nullable=False))
    contact_no = Column(Integer,nullable=False)
    email = Column(String(500),nullable=True,default=None)
    created_at = Column(DateTime,default=datetime.now())
    updated_at = Column(DateTime,default=datetime.now())


