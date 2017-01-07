#!/bin/env python
#coding=utf-8

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index, DateTime,Text,ForeignKey,create_engine
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship,sessionmaker

Base = declarative_base()

class User(Base):

    __tablename__ = 'user'
    uid = Column(Integer,primary_key=True,autoincrement=True)
    email = Column(String(128),unique=True,nullable=False)
    password = Column(String(128),nullable=False)
    reg_time = Column(DateTime(timezone=True),server_default=func.NOW())
    last_time = Column(DateTime(timezone=True),server_default=func.NOW())

def init_db(db_string,admin,pwd):
    print db_string
    engine = create_engine(db_string,echo = True)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    session = sessionmaker(bind=engine,autoflush = True)()
    session.execute("show tables")






